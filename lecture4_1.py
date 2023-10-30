# pip install pysimplegui
import PySimpleGUI as sg
import re

EURO = 1.95576
REGEX = '^[0-9]+([.][0-9]{2})?$'

sg.theme('BluePurple')
layout = [
    [sg.Combo(('EUR', 'BGN'), key='-CURRENCY-IN-', default_value='EUR',
              enable_events=True, readonly=True), sg.InputText(key='-IN-', focus=True),
     sg.Button('Convert')],
    [sg.InputText('BGN', key='-CURRENCY-OUT-', disabled=True, size=(6)),
     sg.InputText(key='-OUT-', disabled=True)]
    #  sg.Text(key='-OUT-')]
]

window = sg.Window('Money Converter', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-CURRENCY-IN-':
        if values['-CURRENCY-IN-'] == 'BGN':
            value = 'EUR'
        else:
            value = 'BGN'
        window['-CURRENCY-OUT-'].update(value)
    # print(values['-IN-'].strip() in ('0123456789.'))
    # if event == 'Convert' and values['-IN-'].isdecimal():
    if event == 'Convert':
        if re.search(REGEX, values['-IN-']):
            if values['-CURRENCY-IN-'] == 'BGN':
                value = float(values['-IN-'])/EURO
            else:
                value = float(values['-IN-'])*EURO
                window['-OUT-'].update(round(value, 2))
        else:
            window['-OUT-'].update('')

window.close()
