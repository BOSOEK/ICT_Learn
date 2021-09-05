# backup-inferface.py
import PySimpleGUI as sg
from pathlib import Path
from backup import backup

sg.theme("DEFAULT1")

col = [
    [sg.CB("압축", key = "-COMP-")],
    [sg.CB("Recursive", key = "-REC-")],
    [sg.T("확장자"), sg.I(key="-EXT-", size=(8, 1), default_text="*.*")]
]

layout = [
    [
        sg.T("원본 폴더를 선택해주세요", size=(20, 1)), 
        sg.In(key="-SRC-", enable_events=True),
        sg.FolderBrowse(target="-SRC-", tooltip="폴더를 입력해 주세요")
    ],
    [
        sg.T("대상 폴더를 선택해주세요", size=(20, 1)), 
        sg.In(key="-DEST-", enable_events=True),
        sg.FolderBrowse(target="-DEST-", tooltip="폴더를 입력해 주세요")
    ],
    [sg.T("파일 목록")],
    [sg.Multiline(size=(45, 20), key="-FILES-"), sg.Col(col)],
    [sg.B("백업", key="-BACKUP-"), sg.Exit()]    
]

window = sg.Window("간단한 백업프로그램", layout)

while True:
    event, values = window.read()
    if event == "-SRC-":
        src = Path(values["-SRC-"])
        files = list(src.rglob(values["-EXT-"]))
        window["-FILES-"].update(value="")
        if files:
            chrs = max([len(str(x)) for x in files])
            for fs in files:
                window["-FILES-"].print(fs)
                window["-FILES-"].set_size(size=(chrs, None))
    elif event == "-DEST-":
        dest = Path(values["-DEST-"])
        empty = next(dest.iterdir(), None)
        if empty:
            btn = sg.popup_ok_cancel("해당 폴더에 파일이 존재합니다")
            if btn == "Cancel":
                window["-DEST-"].update(value="")
    elif event == "-BACKUP-":
        src = Path(values["-SRC-"])
        dest = Path(values["-DEST-"])
        comp = values["-COMP-"]
        rec = values["-REC-"]
        ext = values["-EXT-"]
        backup(src, dest, rec, comp, ext)
        sg.popup("백업이 완료되었습니다")

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # print(event, values)
    