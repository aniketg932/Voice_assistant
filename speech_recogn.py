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
import json

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak up...')
        r.pause_threshold = 0.8
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
    t = datetime.datetime.now().strftime('%I:%M:%p')

    if 0 <= hour <= 12:
        speak(f"Good Morning,its {t}")
    elif 12 <= hour <= 18:
        speak(f"Good Afternoon,its {t}")
    else:
        speak(f"Good Evening,its {t}")
    speak("I am Skye,how can i help you !!")

def news():
    welcome = ["Welcome to The Automated News Reader", "So what you wanna hear?", "lets roll some news"]

    dict1 = {1: "business", 2: "entertainment", 3: "general", 4: "health", 5: "science", 6: "sports", 7: "technology"}
    # dict2 = {1: "in", 2: "23"}

    y = random.choice(welcome)
    speak(y)
    print("1.business\n2.entertainment\n3.general\n4.health\n5.science\n6.sports\n7.technology\n")
    speak(
        "Enter the type of the news you wanna hear: \n1 for business\n2 for entertainment\n3 for general\n4 for health\n5 for science\n6 for sports\n7 for technology\n")
    # print(dict1[x])
    x = int(input("choice: "))
    if x > 7 or x < 1:
        speak("Wrong Choice...Please select a valid input")
        sys.exit()

    else:
        r = requests.get(f"http://newsapi.org/v2/top-headlines?country=in&category={dict1[x]}&apiKey=08aca3a0d644499580c2868e6eb17798")
        data = r.text
        parsed = json.loads(data)
        # print(x,dict2[x])
        #print(parsed)
        speak(f"So these are TOP 5 headlines of {dict1[x]} category")
        for i in range(1,6):
            if (i < 5):
                speak(f"so the number {i} news is ")
                speak(parsed['articles'][i]['title'])
            else:
                speak(f"the last but not the least ")
                speak(parsed['articles'][i]['title'])


def weather():
    API_key = "3c18c5a77fa131312dbdb5974c055e67"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city ="West bengal"
    Final_url = base_url + "appid=" + API_key + "&q=" + city
    weather_data = requests.get(Final_url).json()
    temp = round(weather_data['main']['temp'] - 273.15)
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']


    speak("Temperature is " + str(temp) + " degree celsius.")
    speak("Wind Speed is " + str(wind_speed) + " kilometers per hour.")
    speak(str(description) + " is my prediction")


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
                wb.open(f'https://www.google.com/search?sxsrf=ALeKk00KN9RiA4lwoluF9_ZiM4dyeVqmsw%3A1611300263015&source=hp&ei=pn0KYIHaO6rYz7sP5ZqDgAI&q={str}&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDMTGgCcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab')

        elif "update news" in a:
            speak("Please wait,Its getting load")
            news()

        elif 'blog' in a:
            print('Welcome to my blog posts')
            wb.open('https://aniketguptasite.wordpress.com/')

        elif 'open command prompt' in a:
            os.system('start cmd')

        elif 'my site' in a:
            speak("Welcome to my website")
            wb.open('https://inventivemind.me/')

        elif 'play music' in a:
            music_dir = "C:\\Users\\KIIT\\Music"
            songs = os.listdir(music_dir)
            rm=random.randint(1,40)
            os.startfile(os.path.join(music_dir,songs[rm]))

        elif 'open codeblocks' in a:
            npath="C:\Program Files (x86)\CodeBlocks\\codeblocks.exe"
            os.startfile(npath)

        # elif 'open camera' in a:
        #     cam = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cam.read()
        #         cv2.imshow('webcam',img)
        #         p = cv2.waitKey(50)
        #         if p == 20:
        #             break
        #         cam.release()
        #         cv2.destroyAllWindows()

        elif "open youtube" in a:
            wb.open("https://www.youtube.com/?reload=9")

        elif "wikipedia" in a:
            speak("Searching wikipedia:")
            a = a.replace("wikipedia","")
            results = wikipedia.summary(a, sentences=2)
            speak("according to wikipedia")
            speak(results)

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


        elif "weather" in a or "climate" in a:
            try:
                weather()
            except Exception as e:
                speak("Due to some trouble, i couldn't find the exact weather_data")

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

        #speak("Sir,do you have any other work ??")

if __name__ == '__main__':
    while True:
        pm = command().lower()
        if "wake up" in pm:
            Execution()
        elif "goodbye" in pm:
            speak("Thanks for using me sir,have a good day")
            sys.exit()