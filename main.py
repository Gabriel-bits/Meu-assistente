import speech_recognition as sr 
import pyttsx3


def speak(text):
    souce = pyttsx3.init()
    pyttsx3.voice.Voice(id=None, languages="pt")
    souce.say(text)
    souce.runAndWait()



r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        try:
            audioo = r.listen(s)

            speech = r.recognize_google(audioo, language='pt')

            print(speech)
            # speak(speech)

            if speech in "Olá":
                speak("Oi, tudo bem")
            
            if "tudo e voce ?" in speech:
                speak("aqui ta otimo !")

        except Exception as e:
            print(e)
