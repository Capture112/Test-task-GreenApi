import flet as ft
import requests
from flet import ElevatedButton, Page, Text, TextField, Row

personal_chat = "@c.us"

def main(page: Page):

    #вызов функций кнопок
    def get_Settings_clicked(e):
        url = "https://api.green-api.com/waInstance" + IdInstance.value + "/getSettings/" + APITokenInstance.value
        response = requests.request("GET", url, headers={}, data={})
        result.value = response.text.encode('utf8')
        page.update()
    def get_StateInstance_clicked(e):
        url = "https://api.green-api.com/waInstance" + IdInstance.value + "/getStateInstance/" + APITokenInstance.value
        response = requests.request("GET", url, headers={}, data={})
        result.value = response.text.encode('utf8')
        page.update()
    def send_Message_clicked(e):
        url = "https://api.green-api.com/waInstance" + IdInstance.value + "/sendMessage/" + APITokenInstance.value
        number = number_field.value + personal_chat
        message = message_field.value
        payload = "{\r\n\t\"chatId\": \"" + number + "\",\r\n\t\"message\": \"" + message + "\"\r\n}"
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        result.value = response.text.encode('utf8')
        page.update()
    def send_Pic_clicked(e):
        number = pic_number_field.value + personal_chat
        link = link_field.value
        url = "https://api.green-api.com/waInstance" + IdInstance.value + "/sendFileByUrl/" + APITokenInstance.value
        payload = "{\r\n   \t\"chatId\": \"" + number + "\",\r\n\t\"urlFile\": \"" + link + "\",\r\n\t\"fileName\": \"image.png\"\r\n}"
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        result.value = response.text.encode('utf8')
        page.update()

    #Поля и кнопки
    result = Text()
    output_label = Text("Ответ:")
    IdInstance = TextField(label="IdInstance",value="1103946202")
    APITokenInstance = TextField(label="APITokenInstance",value="81fa8f744b3a4b8484de35d7d2b53283b99e46a30659465aae")
    getstate = ElevatedButton(text="Get_StateInstance", on_click=get_StateInstance_clicked)
    getset = ElevatedButton(text="Get_Settings", on_click=get_Settings_clicked)
    number_field = TextField(label="Введите номер")
    message_field = TextField(label="Введите текст сообщения", value="Hello World!")
    sendMes = ElevatedButton(text="sendMessage", on_click=send_Message_clicked)
    pic_number_field = TextField(label="Введите номер")
    link_field = TextField(label="Укажите ссылку")
    sendPic = ElevatedButton(text="SendFileByurl", on_click=send_Pic_clicked)

    #Левая колонка с вводом
    left_column = ft.Container(ft.Column([
        IdInstance,
        APITokenInstance,
        getstate,
        getset,
        number_field,
        message_field,
        sendMes,
        pic_number_field,
        link_field,
        sendPic
    ]),width=260,height=560)
    #Правая колонка с выводом
    center_column = ft.Container(
        ft.Column([
            output_label,
            result
        ]),
        border_radius=2,
        width=600,
        height=700,
        offset=ft.Offset(x=0.1, y=0)
    )
    page.add(Row([left_column,center_column]))

ft.app(target=main, view=ft.WEB_BROWSER,port=8000)