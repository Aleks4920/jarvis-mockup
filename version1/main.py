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


warnings.filterwarnings('ignore')

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


        say(time.strftime("%H:%M"))


# obtain audio from the microphone
def rest():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('ready')
        audio = r.listen(source)

        print(r.recognize_google(audio, language = 'en', show_all=True))
        return str(r.recognize_google(audio))


def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()


while True:
    i = ""
    try:
        i = rest()
    except:
        pass

    if i !='[]':
        check(i)
