from body.extenção_comds import*
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
from gtts import gTTS
import playsound
import pyaudio
import pyttsx3
import os, json, datetime, asyncio
from fuct import*


class Assitent():
    """
    Corpo do bot
    """
    def __init__(self):
        print("Assistente on")
        
        # try:

        #     self.ouvido = ouvir_comando_on()
        #     resposta('sistema O.C. online inicializado')
        #     self.estado = "on"

        # except Exception as err:
        #     self.ouvido = ouvir_comando()
        #     resposta('devido a falta de NET, vou utilizar o sistema offline')
        #     resposta('então, devido a esta usando o sistema offline, o reconhecimeto vai ser afetado de forma negativa')
        #     self.estado = "off"
        #     print(err)

        # self.Input = ouvir_comando_on()

    def descanço():
        while True:
            Input = ouvir_comando()
            if Input in ("sexta", "sexta feira"):
                resposta('acordei!')
                return
            if Input in ("desligar","desliga","finalizar"):
                sys.exit()


    def comandos(self):

        # if self.estado == 'on':
        #     self.Input = ouvir_comando_on()

        # if self.estado == 'off':
        #     self.Input = ouvir_comando_on()
        # else:
        #     pass
        self.Input = ouvir_comando_on()

        print(self.Input)
        print(1)
        
        #-= comandos base =-#

        #// Suspender
        if 'descansa' in self.Input: 
            resposta('to indo, qualquer coisa e so chamar. vou ficar atenta.')
            Assitent.descanço()
        
        #// Verificar
        elif self.Input in ("oi", "olá", "Oi"): 
            resposta("Oi, tudo bem?")

        #// Horas
        elif "quantas horas" in self.Input: 
            data_hour = datetime.datetime.now()
            resposta(f"são {data_hour.hour} Horas e {data_hour.minute} minutos")


        #-= comandos música =-#

        elif self.Input in ("música tranquila", "música tranquilo", "música acalma", "música calma"):
            Music_on = Music_on_()
            Music_on.music_lo_fi_on()
            
        elif self.Input in ("rock", "música pesada"):
            Music_on = Music_on_()
            Music_on.music_rock_on()

        elif self.Input.lower() in ("aleatoria", "musica aleatoria"):
            Music_on = Music_on_()
            Music_on.music_ale_on()

        elif self.Input in ("musica ambiente", "ambiente"):
            Music_on = Music_on_()
            Music_on.music_ambiente_on()

        elif self.Input in ("parar música", "para a música"):
            Music_on = Music_on_()
            Music_on.parar_musica()


        #-= comandos web =-#

        #// Teste
        elif 'teste' in self.Input: 
            resposta('comando inacabado')

        #// Encerrar o assistente
        elif 'desliga' in self.Input: 
            resposta('encerrando')
            return sys.exit()

        #// Pesquisar as atividades
        elif 'procurar atividade' in self.Input: 
            atividades_base()

        #//  Falar atividades
        elif 'atividades encontradas' in self.Input: 
            extract_ativi()            
