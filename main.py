# Virtual Assistant Projects

# pip install pyttsx3
# pip install speechRecognition
# pip install PyAudio

import speech_recognition as sr
import pyttsx3
import pywhatkit #search online
import datetime
import wikipedia
import webbrowser
import pyjokes
from pywhatkit.remotekit import start_server
from flask import Flask, request

listener = sr.Recognizer()
engine = pyttsx3.init() #initalize
# Define your ideal voices
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    #engine.say('I am your Alexa Nice to meet you')
    #engine.say('What can I do for you')
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening . . .')
            # source is what you are going to say
            voice = listener.lsiten(source)
            command = listener.recognize_google(voice) # Google API -> voice to texts
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa', '')
                engine.say("Did you say ")
                talk(command)
                print(command)
    except:
        pass
    return command

def run_Alexa():
    # take the command
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk(f'playing {song}')
        print(f'Playing . . .{song}')
        pywhatkit.playonyt(song) # play on youtube

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk(f'The time is {time}')

    elif 'Who the hell is' in command:
        person = command.replace('Who the fuck is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)

    elif 'open google' in command:
        talk('Opening google for you')
        webbrowser.open('https://www.google.com/')

    elif 'google research' in command:
        research = command.replace('google research','')
        talk('I am researching')
        pywhatkit.search(research)
        print(research)

    elif 'open schedule' in command:
        talk('opening schedule planner ')
        webbrowser.open('https://ticktick.com/webapp/#q/all/today')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    else:
        talk('I could not understand you ')
        talk('Please say it again')

while True:
    run_Alexa()