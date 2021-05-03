import speech_recognition as sr
from vosk import Model, KaldiRecognizer
from gtts import gTTS
import playsound
import pyaudio
import pyttsx3
import os, json, pygame


#variaveis de fala do bot: 
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-3].id)


#voz do bot
def resposta(texto):
    # pyttsx3.voice.Voice(id=7, languages="pt")
    engine.say(texto)
    engine.runAndWait()


resposta("inicializando")

#variables Vosk-api
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def ouvir_comando():
    #rec.pause_threshold = 1 teste****
    
    data = stream.read(40000)
    rec.AcceptWaveform(data)
    

    result = rec.Result()
    result = json.loads(result)
    Input = str(result['text'])


    return Input.lower()

def ouvir_comando_on():
    # try:
    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)
        audio = r.listen(s)
        speech = r.recognize_google(audio, language= "pt-BR")
        
    # if sr.UnknownValueError:
    #     print("")

    # except sr.UnknownValueError:
    #     print('')

    # except:
    #     raise UnboundLocalError("nada")
    
    return speech


def salvar_ativi(ind, dict):
    with open(f"assets/atividade - {ind}.json", "w") as f:
        json.dump(dict, f)


def ativi_revela(ind):
    with open(f"assets/atividade - {ind}.json", "r") as f:
        data_ativi = json.load(f)
        return data_ativi


def secret():
    with open("secreto.json", "r") as f:
        secreto = json.load(f)
    return secreto


def escam_music(dire):
    """
    Escania as musicas
    """
    loca_m = 'C:/Users/Narutinn/Music/Bot/'
    for root, folder, filer_names in os.walk(loca_m + dire):
        list_musicas = filer_names
    print(list_musicas)
    return list_musicas


def tempo_pause():
    while True:
        1

#   C:\Users\Narutinn\AppData\Local\Programs\Opera GX\73.0.3856.438

#   C:\Users\Narutinn\AppData\Local\Discord\Update.exe --processStart Discord.exe
