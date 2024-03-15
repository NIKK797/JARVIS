import webbrowser
import random
import datetime
import pyttsx3
import wikipedia
import wolframalpha
import math
import os
import speech_recognition as sr
import pywintypes
from random_song import rndm
from opener import open


engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 4].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


currentH = int(datetime.datetime.now().hour)
if currentH >= 0 and currentH < 12:
    speak('Good Morning Boss!')

if currentH >= 12 and currentH < 18:
    speak('Good Afternoon Boss!')

if currentH >= 18 and currentH != 0:
    speak('Good Evening Boss!')

welcome = ['Welcome Boss!', 'Hi Boss!', 'Hello Boss', 'Hello Boss, I Am Friday at your Service!', 'Welcome']
Yup = ["Ok sir!", "Yes Sir", "Sure!"]
Hello = ["Hello Sir!", "Hi", "Howdy!", "Hello!"]


# Movies
iron3 = "explorer E:\movies\Iron_Man_3.mp4"
iron2 = "explorer E:\movies\Iron_Man_2.mp4"

movies = [iron3, iron2]

# Pre Commands
for_music = ["song", "music"]

while True:
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

        if 'hello' in command:
            speak(random.choice(Hello))

        if 'song' in command or 'music' in command:
            speak(random.choice(Yup))
            rndm()

        if 'channel' in command:
            speak(random.choice(Yup))
            webbrowser.open("https://www.youtube.com/channel/UC660FjLvOAxptyGKqmZz88w")

        if 'thank you' in command:
            speak("You're Welcome!")

        if 'how are you' in command:
            speak("I Am Fine!! Thanks For Asking!!!")

        if 'search' in command: 
            speak("Searching...")
            webbrowser.open(command)


        if "open" in command:
            speak("Opening...")
            open(command)


        if "who are you" in command:
            speak("I am JARVIS")

        



    except:
        pass













