# calculator.py

import PySimpleGUI as sg

col1 = [
    [sg.B("7", size=(4, 2)), sg.B("8", size=(4, 2)), sg.B("9", size=(4, 2))],
    [sg.B("4", size=(4, 2)), sg.B("5", size=(4, 2)), sg.B("6", size=(4, 2))],
    [sg.B("1", size=(4, 2)), sg.B("2", size=(4, 2)), sg.B("3", size=(4, 2))],
    [sg.B("/", size=(4, 2), key="-DIV-"), sg.B("0", size=(4, 2)), sg.B("", size=(4, 2))],
]

col2 = [
    [sg.B("x", size=(4, 2), key="-MUL-")],
    [sg.B("-", size=(4, 2), key="-SUB-")],
    [sg.B("+", size=(4, 2), key="-ADD-")],
    [sg.B("=", size=(4, 2), key="-EQL-")],
]

layout = [
    [sg.I(size=(10, 1), font=(None, 30), key="-DISP-")],
    [sg.Col(col1), sg.VSep(), sg.Col(col2)]
]

window = sg.Window("나만의 계산기", layout)

# 계산기 로직 구현
nums = [str(x) for x in list(range(0, 10))]
num = ""

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event in ["-MUL-", "-SUB-", "-ADD-", "-DIV-"]:
        num1 = values["-DISP-"]
        window["-DISP-"].update("")
        num = ""
        operation = event
    elif event in nums:
        num += event
        window["-DISP-"].update(num)
    elif event == "-EQL-":
        num1 = float(num1)
        num2 = float(values["-DISP-"])
        if operation == "-ADD-":
            res = num1 + num2
        elif operation == "-SUB-":
            res = num1 - num2
        elif operation == "-MUL-":
            res = num1 * num2
        elif operation == "-DIV-":
            res = num1 / num2  
        window["-DISP-"].update(int(res))                      