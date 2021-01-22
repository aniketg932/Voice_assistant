# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from voice import engine

def speak(str):
    engine.say(str)
    engine.runAndWait()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    speak("Hello, How are You!!")
    speak("Name- Aniket Kumar Gupta")
    speak("Prime's Gaming - Please Like and Subscribe")
