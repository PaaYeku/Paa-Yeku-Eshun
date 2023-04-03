import PySimpleGUI as sg
import pyttsx3

ENGINE = pyttsx3.init()
VOICE = ENGINE.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='black',background_color='yellow'),sg.Radio('Male', 'RADIO1', default=True, key='male',background_color='blue'),sg.Radio('Female', 'RADIO1', key='female',background_color='pink')],
     [sg.Text('Enter text to speak:',text_color='black',background_color='green',)],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='red')],
   
    
]

window = sg.Window('Soleil', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male']:
            ENGINE.setProperty('voice', VOICE[0].id)
        elif values['female']:
           ENGINE.setProperty('voice', VOICE[1].id) 
    
        ENGINE.say(text)
        ENGINE.runAndWait()

window.close()