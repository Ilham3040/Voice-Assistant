from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.config import Config
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'say hello' in command:
        print("hello")
        talk('hello there my name is alexa can i help you?')
    else:
        talk('Please say the command again.')



def run(instance):
    run_alexa()


class MyApp(App):
    
    def build(self):
        self.title = "Ilham App"
        layout = AnchorLayout(anchor_x ="center" , anchor_y = "center" ,)
        btn = Button(size_hint=(0.18,0.22),background_normal = 'voice2.png')
        btn.bind(on_press = run)
        layout.add_widget(btn)
        return layout
    

MyApp().run()
