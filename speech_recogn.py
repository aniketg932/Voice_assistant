import speech_recognition as sr
from voice import engine
import webbrowser as wb
import wikipedia

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('[Search mine]')
        print('speak now')
        audio=r.listen(source)

    try:
        query=r.recognize_google(audio,language="en-in")
        print(f"{query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return  query

if __name__ == '__main__':
    a=command().lower()
    if 'hello' in a:
        speak('hi sir, how can i help you !')

    elif 'google' in a:
        print('Open Google !!')
        speak('Say about the query ??')
        str=command().lower()
        if 'page' in str:
            wb.open('https://www.google.com/')
        else:
            wb.open(f'https://www.google.com/search?sxsrf=ALeKk00KN9RiA4lwoluF9_ZiM4dyeVqmsw%3A1611300263015&source=hp&ei=pn0KYIHaO6rYz7sP5ZqDgAI&q={str}&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDMTGgCcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab')

    elif 'blog' in a:
        print('Welcome to my blog posts.')
        wb.open('https://aniketguptasite.wordpress.com/')

    else:
        pass