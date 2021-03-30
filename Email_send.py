# import smtplib
# import speech_recognition as sr
# listen =sr.Recognizer()
# try:
# except:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login('aniketgp5529@gmail.com', 'alanwalker@5535')
#         server.sendmail('aniketgp5529@gmail.com',
#                         'abhishekgp63@gmail.com',
#                         'Hi, bro how are you' )



import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage   #The central class in the email package is the EmailMessage class, imported from the email.message module.
# It is the base class for the email object model. EmailMessage provides the core functionality for setting and querying header fields,
# for accessing message bodies, and for creating or modifying structured messages.

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening to port')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    server.starttls()
    server.login('aniketgp5529@gmail.com','alanwalker@5535')
    email = EmailMessage()
    email['From'] = 'aniketgp5529@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'aniket':'abhishekgp63@gmail.com',
    'alexa':'1828045@kiit.ac.in',
    'harry':'1828052@kiit.ac.in'
}

def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)

    talk('What is the subject of your email?')
    subject = get_info()

    talk('Tell me the text in your email')
    message = get_info()

    send_email(receiver, subject, message)
    talk('Hey lazy.Your email is sent')
    talk('Do you want to send more email?')

    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    else:
        talk("Thank You for your time.")
        print("Thank You for your time.")

get_email_info()