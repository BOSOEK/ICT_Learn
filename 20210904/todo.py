import PySimpleGUI as sg

layout = [
    [
        sg.T("", size=(8, 1), key="-DATE-"), 
        sg.CalendarButton("날짜 설정"), 
        sg.I(key="-TASK-", size=(30, 1))
    ],
    [sg.Ok(), sg.Cancel()]
]

window = sg.Window("Todo 관리", layout)

def create_task(tasks):
    layout = [
        [
            sg.T("", size=(8, 1), key="-DATE-"), 
            sg.CalendarButton("날짜 설정"), 
            sg.I(key="-TASK-", size=(30, 1))
        ]
    ]
    layout += [
        [
            sg.T(idx, size=(3, 1)), 
            sg.T(t, size=(20, 1), key=f"-TX-{idx}"),
            sg.T("x", key=f"-DEL-{idx}", enable_events=True)
        ]
        for idx, t in enumerate(tasks, start = 1)
    ]
    layout += [[sg.Ok(), sg.Cancel()]]
    window1 = sg.Window("Todo 관리 목록", layout)
    return window1

tasks = []
while True:
    event, values = window.read()
    if event in ["Cancel", sg.WIN_CLOSED]:
        break
    elif event == "Ok":
        task = window["-DATE-"].get().split(" ")[0] + " 에 " + values["-TASK-"]
        if task not in tasks:
            tasks.append(task)
        window1 = create_task(tasks)
        window.close()
        window = window1
    elif event.startswith("-DEL-"):
        idx = int(event.split("-DEL-")[-1]) - 1
        if tasks:
            del tasks[idx]
        window1 = create_task(tasks)
        window.close()
        window = window1

    print(event, values, tasks)