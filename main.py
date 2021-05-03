import speech_recognition as sr
from vosk import Model, KaldiRecognizer
from gtts import gTTS
import pyaudio
import pyttsx3
import os, json
import datetime
from fuct import*


# -=- Foldes import -=- #

from body.head import Assitent

# -=- ======+====== -=- #

Assisten = Assitent()

while True:
    try:
        Assisten.comandos()

    except sr.UnknownValueError:
        print("\r")
        pass
        
    except Exception as er:
        resposta("ocorreu um erro senhor.")
        resposta(f"o erro foi... {er}")
        print(f"tai o {er}")
        pass
    # Assisten.comandos()

