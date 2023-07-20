import pytesseract
import pytesseract as PY
from PIL import Image
import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [
    [sg.Text("введите путь до картинки"), sg.InputText(key="-INPUT-")],
    [sg.Button("Отправить"), sg.Button("Закрыть")],
    [sg.Button("Просто кнопка :)")],
    [sg.Checkbox("text", key='s1', checkbox_color='red')]
]

window = sg.Window("Получить число с картинки", layout)
while True:
    events, values = window.read()
    if events == "Закрыть" or events == sg.WIN_CLOSED:
        break
    elif events == "Отправить":
        img = Image.open(str(values["-INPUT-"]))
        text = pytesseract.image_to_string(img)
        print(text)


window.close()




# img=Image.open("/home/kornil/Загрузки/test.png")
# text = pytesseract.image_to_string(img)
# print(text)