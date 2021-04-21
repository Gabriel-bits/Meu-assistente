from body.extenção_comds import*
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
from gtts import gTTS
import playsound
import pyaudio
import pyttsx3
import os, json, datetime
from fuct import*


class Assitent():
    """
    Corpo do bot
    """
    def __init__(self):
        print("Assistente on")
        pass
    
    def descanço():
        while True:
            Input = ouvir_comando()
            if Input in ("sexta", "sexta feira"):
                resposta('acordei!')
                return


    def comandos(self):
        
        while True:
            
            self.Input = ouvir_comando().lower()
            print(self.Input)
            
            #-= comandos base =-#

            #// Suspender
            if 'descansa' in self.Input: 
                resposta('to indo, qualquer coisa e so chamar. vou ficar atenta.')
                Assitent.descanço()
            
            #// Verificar
            if self.Input in ("oi", "olá"): 
                resposta("Oi, tudo bem?")

            #// Horas
            if "quantas horas" in self.Input: 
                data_hour = datetime.datetime.now()
                resposta(f"são {data_hour.hour} Horas e {data_hour.minute} minutos")

            #-= comandos web =-#

            #// Teste
            if 'teste' in self.Input: 
                resposta('comando inacabado')

            #// Encerrar o assistente
            if 'desliga' in self.Input: 
                resposta('encerrando')
                return

            #// Pesquisar as atividades
            if 'procurar atividade' in self.Input: 
                atividades_base()

            #//  Falar atividades
            if 'atividades encontradas' in self.Input: 
                extract_ativi()            
