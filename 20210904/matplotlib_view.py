# matplotlib_viewer.py

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib

layout = [
    [sg.Text('그래프 그리기')],
    [sg.Canvas(key = '-CANVAS-')],
    [sg.Button('OK')]
]

window = sg.Window('Matplotlib 단일 그래프', layout, location=(0, 0), finalize=True, element_justification='center', font='Helvetica 25')

flg = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arang(0, 3, 0.1)
flg.add_subplot(111).plot(t, 2*np.sin(2*np.pi*t))

matplotlib.use('TkAgg')

figure_canvas_agg = FigureCanvasTkAgg(flg, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack(size='top', file='both', expand=1)

event, values = window.read()
window.close()