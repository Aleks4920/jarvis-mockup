
import speech_recognition as sr
import warnings
import time
from datetime import datetime
import weather
from gtts import gTTS
import winsound
import playsound
import os
import news
import chuckNorris
import multiprocessing
from multiprocessing import Process
import commandlist

def say(text):
    myobj = gTTS(text=text, lang='en', slow=False, tld='ca')
    myobj.save("jarvis.mp3")
    playsound.playsound('jarvis.mp3', True)
    os.remove("jarvis.mp3")



def check(i):
    x = i.split(" ")
    if i == "hello":
        say('hello')
    elif  i == 'quit' or i == 'exit' or i == 'shut down' or i == 'stop':
        exit()
    elif 'weather' in i:
        if 'in' in i:
            print(weather.local())
        else:
            say(str(weather.local()))

    elif 'Chuck Norris fact' in i:
        say(chuckNorris.fact())

    elif 'news' in i:
        say(news.latest())
    elif 'time' in i:
        if 'in' in i:
            pass ###############################################################


        say(time.strftime("%H:%M:%S", t))
