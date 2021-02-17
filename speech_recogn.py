import requests
import speech_recognition as sr
from voice import engine
import webbrowser as wb
import os
import cv2
import random
import wikipedia
import pywhatkit as pk
import sys
from weather import weather
import datetime
import time

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak up...')
        r.pause_threshold = 1
        print('Recognizing....')
        audio = r.listen(source,timeout=10, phrase_time_limit=10)

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def wish():
    #speak("Hello sir")
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")

    if 0 <= hour <= 12:
        speak(f"Good Morning,its {t}")
    elif 12 <= hour <= 18:
        speak(f"Good Afternoon,its {t}")
    else:
        speak(f"Good Evening,its {t}")
    speak("I am Skye,how can i help you !!")

def news():
    url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=437c65dddca5420a8e5d3801124077b5'
    page = requests.get(url).json()
    articles = page["articles"]
    head = []
    day=["1","2","3","4","5"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"{day[i]} news: {head[i]}")


#if __name__ == '__main__':
def Execution():
    wish()
    while True:
        a = command().lower()
        if 'google' in a:
            speak('Sir,what should i search for you ??')
            string = command().lower()
            if 'page' in string:
                wb.open('https://www.google.com/')
            else:
                wb.open(
                    f'https://www.google.com/search?sxsrf=ALeKk00KN9RiA4lwoluF9_ZiM4dyeVqmsw%3A1611300263015&source=hp&ei=pn0KYIHaO6rYz7sP5ZqDgAI&q={str}&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDMTGgCcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab')

        elif "update news" in a:
            speak("Please wait,Its getting load")
            news()

        elif 'blog' in a:
            print('Welcome to my blog posts')
            wb.open('https://aniketguptasite.wordpress.com/')

        elif 'about weather' in a:
            weather()

        elif 'open command prompt' in a:
            os.system('start cmd')

        elif 'my site' in a:
            speak("Welcome to my website")
            wb.open('https://inventivemind.me/')

        elif 'play music' in a:
            music_dir = "C:\\Users\\KIIT\\Music"
            songs = os.listdir(music_dir)
            rm = random.choice(songs)
            os.startfile(os.path.join(music_dir, rm))

        elif 'open codeblocks' in a:
            npath = "C:\Program Files (x86)\CodeBlocks\\codeblocks.exe"
            os.startfile(npath)

        elif 'open camera' in a:
            cam = cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow('webcam',img)
                p = cv2.waitKey(50)
                if p == 20:
                    break
                cam.release()
                cv2.destroyAllWindows()

        elif "open youtube" in a:
            wb.open("https://www.youtube.com/?reload=9")

        elif "wikipedia" in a:
            speak("Searching wikipedia:")
            a = a.replace("wikipedia","")
            results = wikipedia.summary(a, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "send message" in a:
            # take a maximum gap of 2 min
            pk.sendwhatmsg("+917606895156","Hi,it's me Aniket",10,10)

        elif "play song on youtube" in a:
            pk.playonyt("We The Kings-Sad Song")


        elif "set an alarm" in a:
            t=int(datetime.datetime.now().hour)
            if t==20:
                music_dir = "C:\\Users\\KIIT\\Music"
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

        elif "shut down" in a:
            os.system("shutdown /s /t 5")

        elif "restart system" in a:
            os.system("shutdown /r /t 5")

        #elif "sleep system" in a:
        #os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "hello" in a or "hi" in a:
            speak("Hello sir, how can i help you?")

        elif "how are you" in a:
            speak("I am fine, what about you!")

        elif "me also good" in a or "me fine" in a:
            speak("That's great to hear from you sir.")

        elif "thank you" in a:
            speak("It's my plasure for you sir.")

        elif "you may sleep now,skye" in a or "go to sleep,skye" in a:
            speak("Okay sir,I am going to sleep you can call me anytime")
            break

        elif "thanks" in a:
            speak("Thanks for taking my help sir,Have a good day!!")
            sys.exit()

        #speak("Sir,do you have any other work??")

if __name__ == '__main__':
    while True:
        pm = command().lower()
        if "wake up" in pm:
            Execution()
        elif "goodbye" in pm:
            speak("Thanks for using me sir,have a good day")
            sys.exit()

