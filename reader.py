from win32com.client import Dispatch
import json
import random
import sys

welcome=["Welcome to The Automated News Reader","So what you wanna hear?","lets roll some news"]

dict1={1:"business",2:"entertainment",3:"general",4:"health",5:"science",6:"sports",7:"technology"}
dict2={1:"in",2:"23"}

def speak(str):
        speak=Dispatch("SAPI.SpVoice")
        speak.Speak(str)

if __name__ == '__main__':
    import requests
    y=random.choice(welcome)
    speak(y)
    print("1.business\n2.entertainment\n3.general\n4.health\n5.science\n6.sports\n7.technology\n")
    speak("Enter the type of the news you wanna hear: \n1 for business\n2 for entertainment\n3 for general\n4 for health\n5 for science\n6 for sports\n7 for technology\n")
    # print(dict1[x])
    x=int(input("choice: "))
    if x>7 or x<1:
        speak("Wrong Choice...Please select a valid input")
        sys.exit()

    else:
        r=requests.get(f"http://newsapi.org/v2/top-headlines?country=in&category={dict1[x]}&apiKey=08aca3a0d644499580c2868e6eb17798")
        data=r.text
        parsed=json.loads(data)
        # print(x,dict2[x])
        print(parsed)
        speak(f"So these are TOP 5 headlines of {dict1[x]} category")
        for i in range(1,6):
                if(i<5):

                    speak(f"so the number {i} news is ")
                    print(parsed['articles'][i]['title'])
                    speak(parsed['articles'][i]['title'])
                else:
                    speak(f"the last but not the least ")
                    print(parsed['articles'][i]['title'])
                    speak(parsed['articles'][i]['title'])