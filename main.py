import playsound
import pyaudio
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from vosk import Model, KaldiRecognizer
import os, json

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-3].id)

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def resposta(texto):
    # pyttsx3.voice.Voice(id=1, languages="pt")
    engine.say(texto)
    engine.runAndWait()

resposta("inicializando")

def ouvir_comando():
    rec.pause_threshold = 1
    data = stream.read(10000)
    rec.AcceptWaveform(data)

    result = rec.Result()
    result = json.loads(result)
    Input = str(result['text']).lower()


    return Input

while True:

    Input = ouvir_comando()
    print(Input)

    if Input is not None:
        if "olá" in Input:
            resposta("Oi, tudo bem ?")

