import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.Popup("Pop\n(c) 2023 Erik's Gadgets")
pop_layout = [[sg.Input(), sg.Button("SAVE")], [sg.Button("OPEN")]]
pop_win = sg.Window("Pop", pop_layout)
pop_query = []

while True:
    event, values = pop_win.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "SAVE":
        pop_query.append(values[0])
    if event == "OPEN":
        sublayout = [[]]
        for i in pop_query:
          sublayout[0].append(i)
          previous = ""
          for k in sublayout[0]: 
            previous += str(k)
            previous += "\n"
        sg.Popup("Previous Queries", previous)
        del sublayout
        del previous
              
              
pop_win.close()
