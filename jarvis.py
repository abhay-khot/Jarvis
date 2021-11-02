import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

NAME = "Abhay"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 6 and hour < 12:
        speak("Good morining" + NAME)

    elif hour >= 12 and hour < 16:
        speak("Good afternoon" + NAME)

    else:
        speak("Good night" + NAME)

    # speak("I am Jarvis. How may I help you")


# Takes command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Please say that again")
        query = None

    return query


def sendEmail(to, contact):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Add email id and password to login from this server.
    server.login('', '')
    server.sendmail('', to, content)  # Add reciever's email id
    server.close()


speak("Intializing Jarvis.....")


def main():

    wishMe()
    query = takeCommand()
    query = query.lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        url = "youtube.com"

        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query:
        url = "google.com"

        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query:
        songsDir = ""  # Add the directory address

        songs = os.listdir(songsDir)
        print(songs)
        os.startfile(os.path.join(songsDir, songs[0]))

    elif 'send email' in query:
        try:
            speak("What should I send")
            content = takeCommand()
            to = ""  # Add recievers email address
            sendEmail(to, content)
            speak("Email has been sent")

        except Exception as e:
            print(e)


main()
