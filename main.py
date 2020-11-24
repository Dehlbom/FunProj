import PySimpleGUI as sg
#TODO
#Läsa och skriva till en textfil



sg.theme('DarkAmber')


Stats = [1, 2, 3, 4, 5]

# Define the window's contents
layout1 = [[sg.Button('Start page'), sg.Button('Statistics'), sg.Button('Transactions'), sg.Button('Plots')],
          [sg.Text("Expenses")],
          
          #[sg.Input(key='-INPUT-')],
          #[sg.Text(size=(40,1), key='-OUTPUT-')],
          #[sg.Button('Ok'), sg.Button('Quit')]]

layout2 = [[sg.Button('Start page'), sg.Button('Statistics'), sg.Button('Transactions'), sg.Button('Plots')],
          [sg.Text("New expense")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

layout3 = [[sg.Button('Start page'), sg.Button('Statistics'), sg.Button('Transactions'), sg.Button('Plots')],
          [sg.Text("New expense")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

layout4 = [[sg.Button('Start page'), sg.Button('Statistics'), sg.Button('Transactions'), sg.Button('Plots')],
          [sg.Text("New expense")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('PyProj', layout1)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()