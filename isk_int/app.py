import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk('привет,спроси что-нибудь') #слова робота talk()

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source: #Микрофон
        print('Говорите')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print('Вы сказали: ' + zadanie)
    except sr.UnknownValueError:
        talk('я вас не понимаю')
        zadanie = command()
    
    return zadanie

def makesmth(zadanie):
    if 'open website' in zadanie:
        url = 'https://vk.com/tungaa3109'
        webbrowser.open(url)
    elif 'stop' in zadanie:
        talk('да, конечно, без проблем')
        sys.exit() #выйти из приложения

while True:
    makesmth(command())

