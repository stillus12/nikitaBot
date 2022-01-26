# Сделано Егором в 2022 году
# Puchckov Industries ©

# мой говорящий помошник(как алиса из яндекс)

# библиотеки(импорт)
import os
import time

import speech_recognition as sr
import pyttsx3
import datetime
from fuzzywuzzy import fuzz

# настройки разговора с человеком
options = {
    "alias": ('никита', 'никит', 'никитос', 'Никита'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
    "cmd": {
        "ctime": ('сколько сейчас времени', 'сколько времени', 'какое сейчас время', 'сейчас времени', 'какой час', 'время', 'сколько сейчас времени'),
        "radio": ('включи музыку', 'музыка'),
        "browser": ('открой браузер', 'Открой браузер'),
        "vscode":('открой среду для програмировния', 'Открой среду для програмировния'),
        "krut":('ты крутой', 'Ты крутой'),
        "exit":('можешь выключиться', 'Можешь выключиться')
    }
}

def speak(what):
    print( what )
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU")
        print("Я распознавал: " + voice)
        if(voice.startswith(options["alias"])):
            # обращение
            cmd = voice

            for x in options['alias']:
                cmd = cmd.replace(x, "").strip()
                print(cmd)

            for x in options['tbr']:
                cmd = cmd.replace(x, "").strip()
                print(cmd)

            # распознавание
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
            print(cmd)



    except sr.UnknownValueError:
            print("Голос не распознавал")

    except sr.RequestError as e:
        print("Ошибка подключения к серверу! код ошибки:" + e)



def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    print(RC)
    for c,v in options['cmd'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        # время
        now = datetime.datetime.now()
        speak("Сейчас: " + str(now.hour) + ":" + str(now.minute))
        return True

    if cmd == 'browser':
        # браузер
        os.startfile('C:/Program Files/Google/Chrome/Application/chrome.exe')
        return True

    if cmd == 'krut':
        # ты крутой
        speak("Большое спасибо, а ещё моему создателю Егору")
        return True

    if cmd == 'vscode':
        # vscode
        os.startfile('C:/Users/Егорик/AppData/Local/Programs/Microsoft VS Code/Code.exe')
        return True

    if cmd == 'exit':
        # пока
        speak("Пока!")
        exit()

    else:
        speak("Такой команды нет базе данных")


# создание доступа(запуск)

r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

# инициализация голоса

speak_engine = pyttsx3.init()

print("Puchckov Industries ©")
speak("Привет!")
speak("Это бот никита")


# включаем слушателя
stop_l = r.listen_in_background(m, callback)

while True:
    pass
