# pip install opencv-python
​
import PySimpleGUI as sg
import cv2
import numpy as np
​
layout = [
    [sg.Text("OpenCV 프로그램", size=(60, 1), justification="center")],
    [sg.Image(filename="", key="-IMAGE-")],
    [sg.Radio("None", "Radio", True, size=(10, 1), key="-NONE-")],
    [
        sg.Radio("threshold", "Radio", size=(10, 1), key="-THRESH-"), 
        sg.Slider((0, 255), 128, 1, orientation="h", size=(40, 15), key="-THRESH_VALUE-")
    ],
    [
        sg.Radio("canny", "Radio", size=(10, 1), key="-CANNY-"),
        sg.Slider((0, 255), 128, 1, orientation="h", size=(20, 15), key="-CANNYA-"),
        sg.Slider((0, 255), 128, 1, orientation="h", size=(20, 15), key="-CANNYB-")
    ],
    [
        sg.Radio("blur", "Radio", size=(10, 1), key="-BLUR-"),
        sg.Slider((1, 11), 1, 1, orientation="h", size=(40, 15), key="-BLUR_VALUE-")
    ],
    [   
        sg.Radio("hue", "Radio", size=(10, 1), key="-HUE-"),
        sg.Slider((0, 255), 0, 1, orientation="h", size=(40, 15), key="-HUE_VALUE-")
    ],
    [
        sg.Radio("enhance", "Radio", size=(10, 1), key="-ENHANCE-"),
        sg.Slider((1, 255), 128, 1, orientation="h", size=(40, 15), key="-ENHANCE_VALUE-")
    ],
    [sg.Button("나가기", size=(10, 1))]
]
​
window = sg.Window("PySimpleGUI로 만든 OpenCV 프로그램", layout, location = (800, 400))
​
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
​
while True:
    event, values = window.read(timeout=20)
    if event == "나가기" or event == sg.WIN_CLOSED:
        break
​
    ret, frame = cap.read()
​
    if values["-THRESH-"]:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)[:, :, 0]
        frmae = cv2.threshold(
            frame, values["-THRESH_VALUE-"], 255, cv2.THRESH_BINARY
        )[1]
    elif values["-CANNY-"]:
        frame = cv2.Canny(
            frame, values["-CANNY SLIDER A-"],
            values["-CANNY SLIDER B-"]
        )
    elif values["-BLUR-"]:
        frame = cv2.GaussianBlur(
            frame,
            (21, 21),
            values["-BLUR SLIDER-"]
        )
    elif values["-HUE-"]:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame[:, :, 0] += int(values["-HUE SLIDER-"])
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    elif values["-ENHANCE-"]:
        enh_val = values["-ENHANCE SLIDER-"] / 40
        clahe = cv2.createCLAHE(
            clipLimit=enh_val, tileGridSize=(8, 8)
        )
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        lab[:, :, 0] = clahe.apply(lab[:, :, 0])
        frame = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
​
    imgbytes = cv2.imencode(".png", frame)[1].tobytes()
    window["-IMAGE-"].update(data=imgbytes)