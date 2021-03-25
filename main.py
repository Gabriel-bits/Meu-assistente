import speech_recognition as sr 
import pyttsx3
from gtts import gTTS
import playsound
import pyaudio
from vosk import Model, KaldiRecognizer
import os

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())

# def speak(text):
#     souce = pyttsx3.init()
#     pyttsx3.voice.Voice(id=None, languages="pt")
#     souce.say(text)
#     souce.runAndWait()



# r = sr.Recognizer()

# with sr.Microphone() as m:
#     r.adjust_for_ambient_noise(m)

#     while True:
#         try:

#             audioo = r.listen(m)
#             speech = r.recognize_google(audioo, language='pt')

#             print(speech)
#             # speak(speech)

#             if speech in "Olá":
#                 speak("Oi, tudo bem")
            
#             if "Tudo e você" in speech:
#                 speak("aqui ta ótimo!")

#         except Exception as e:
#             print(e)
