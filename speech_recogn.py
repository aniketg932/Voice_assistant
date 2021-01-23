import speech_recognition as sr
from voice import engine
import webbrowser as wb
import os
import datetime
import cv2
import random
import wikipedia
import pywhatkit as pk
import sys

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak up...')
        r.pause_threshold=1
        print('Recognizing....')
        audio=r.listen(source,timeout=5,phrase_time_limit=5)

    try:
        query=r.recognize_google(audio,language="en-in")
        print(f"User said {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
        #print("Good morning.")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
        #print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")
    speak("I am Skye,how can i help you !!")


if __name__ == '__main__':
    wish()
    while True:
        a = command().lower()
        if 'google' in a:
            speak('Sir,what should i search for you ??')
            string = command().lower()
            if 'page' in string:
                wb.open('https://www.google.com/')
            else:
                wb.open(f'https://www.google.com/search?sxsrf=ALeKk00KN9RiA4lwoluF9_ZiM4dyeVqmsw%3A1611300263015&source=hp&ei=pn0KYIHaO6rYz7sP5ZqDgAI&q={str}&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDMTGgCcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab')

        elif 'blog' in a:
            print('Welcome to my blog posts.')
            wb.open('https://aniketguptasite.wordpress.com/')

        elif 'open command prompt' in a:
            os.system('start cmd')

        elif 'my site' in a:
            speak("Welcome to my website")
            wb.open('https://inventivemind.me/')

        elif 'play music' in a:
            music_dir = "C:\\Users\\KIIT\\Music"
            songs = os.listdir(music_dir)
            rm=random.choice(songs)
            os.startfile(os.path.join(music_dir,rm))

        elif 'open codeblocks' in a:
            npath="C:\Program Files (x86)\CodeBlocks\\codeblocks.exe"
            os.startfile(npath)

        elif 'open camera' in a:
            cam=cv2.VideoCapture(0)
            while True:
                ret,img=cam.read()
                cv2.imshow('webcam',img)
                p=cv2.waitKey(50)
                if p==20:
                    break
                cam.release()
                cv2.destroyAllWindows()

        elif "open youtube" in a:
            wb.open("https://www.youtube.com/?reload=9")

        elif "wikipedia" in a:
            speak("Searching wikipedia:")
            a=a.replace("wikipedia","")
            results=wikipedia.summary(a,sentences=4)
            speak("according to wikipedia")
            speak(results)

        elif "send message" in a:
            #take a maximum gap of 2 min
            pk.sendwhatmsg("+917606895156","Hi,it's me Aniket",10,10)

        elif "play song on youtube" in a:
            pk.playonyt("We The Kings-Sad Song")

        elif "no thanks" in a:
            speak("Thanks for taking my help sir,Have a good day!!")
            sys.exit()

        speak("Sir,do you have any other work??")