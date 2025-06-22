import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import pyautogui
import pywhatkit
import os
import wikipedia
import psutil
import datetime

name = input
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = datetime.datetime.now().hour
    if hour >=0 and hour <12:
        print(f"good morning{name}")
        speak(f"good morning{name}")
    elif hour >=12 and hour <16:
        print(f"good afternoon {name}")
        speak(f"good afternoon {name}")
    else:
        print(f"good evening {name}")
        speak(f"good evening {name}")
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..........")
        speak("listening......")
        audio=r.listen(source)
    try:
        print("recognizing.....")    
        query=r.recognize_google(audio,language='en-in')
        print(f"you say : {query}")
    except:
        print("say that again")
        speak("say that again")
        return "none"
    return query
# def getweather():

while True:
    q = takecommand().lower()
    greeting_q = ["hello", "hiiii"]
    greeting_a = ["hello dear,Welcome", "Hi! I am always there for you"]

    if q in greeting_q:
        speak(random.choice(greeting_a))
        a = random.choice(greeting_a)
    elif "how are you" in q:
        speak("I am fine")
    elif "open google" in q:
        speak("opening google.....")
        speak("what do you want to browse")
        print("what do you want to browse")
        a= takecommand().lower()
        pywhatkit.search(a)
    elif 'volume up' in q:
        speak("volume increasing")    
        pyautogui.press("volumeup")
    elif 'volume down' in q:
        speak("volume decreasing")    
        pyautogui.press("volumedown")
    elif 'volume mute' in q:
        speak("muting volume")    
        pyautogui.press("volumemute")
    elif 'open notepad' in q:
        speak("opening notepad...")    
        os.startfile("C:\\Windows\\notepad.exe")
        q= takecommand().lower()
    elif'write it down'in q:
        speak("writing it down")
        a = takecommand().lower()
        pyautogui.typewrite(a,0.1)
    elif 'what is' in q:
        speak("searching wikipedia.....")
        qu = q.replace('what is','')
        speak("according to wikipedia")
        print(wikipedia.summary(qu,sentences=3))
        speak(wikipedia.summary(qu,sentences=3))
    elif 'who is' in q:
        speak("searching wikipedia.....")
        qu = q.replace('who is','')
        speak("according to wikipedia")
        print(wikipedia.summary(qu,sentences=3))
        speak(wikipedia.summary(qu,sentences=3))
    elif 'battery' in q:
        battery = psutil.sensors_battery()
        speak(f"battery is {battery.percent} percent")
        print(f"battery is {battery.percent} percent")
    elif 'exit' in q:
        speak("Ok I am going offline")
        exit()
    

    