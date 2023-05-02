from playsound import playsound
import os
from time import sleep
from gtts import gTTS

# Using Google's Text-to-Speech speech synthesis. Commonly used in Google Translate
def speech(text):
    tts = gTTS(text=text, lang='en', slow=False, tld="com.au")
    speech = '/tmp/speech.mp3'
    tts.save(speech)
    playsound(speech)
    #os.remove(speech)    