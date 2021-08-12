from body.extenção_comds import*
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
from gtts import gTTS
import playsound
import pyaudio
import pyttsx3
import os, json, datetime, asyncio
from fuct import*


class Assistent():
    """
    Corpo do bot
    """
    def __init__(self):
        print("Assistente on")
        self.__NOME = 'azul'
        self.estado = True
        
        # try:

        #     self.ouvido = ouvir_comando_on()
        #     resposta('sistema O.C. online inicializado')
        #     self.estado = "on"

        # except Exception as err:
        self.__ouvido = ouvir_comando()
        #     resposta('devido a falta de NET, vou utilizar o sistema offline')
        #     resposta('então, devido a esta usando o sistema offline, o reconhecimeto vai ser afetado de forma negativa')
        #     self.estado = "off"
        #     print(err)

        # self.Input = ouvir_comando_on()

    def descanço(self):
        while True:
            Input = ouvir_comando()
            if self.__NOME in Input:
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
        self.Input = ouvir_comando()

        print(self.Input)
        print(1)
        
        #-= comandos base =-#

        #// Nome
        if 'seu nome' in self.Input:
            resposta(f'Meu nome e {self.__NOME}')

        #// Suspender
        if 'descansa' in self.Input: 
            resposta('to indo, qualquer coisa e so chamar. vou ficar atenta.')
            Assistent.descanço()
        
        #// Verificar
        elif self.Input in ("oi", "olá", "Oi", self.__NOME): 
            resposta("Oi, tudo bem?")

        #// Horas
        elif "quantas horas" in self.Input: 
            horas = datetime.datetime.now()
            resposta(f"são {horas.hour} Horas e {horas.minute} minutos")

        #// Data atual
        elif "data de hoje" in self.Input:
            data = datetime.datetime.now()
            resposta(f" hoje e dia {data.day} do mes {data.month}")

        #// Ano atual
        elif "ano atual" in self.Input:
            data = datetime.datetime.now()
            resposta(f" estamos no ano de {data.year}")


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


        ##


        #-= execução de apps =-#

        #// Teste
        elif 'teste' in self.Input: 
            resposta('1,2,3 testando. Meu audio esta funcionando !')

        #// Meu navegador
        elif self.Input in ('o google', 'google'):
            resposta('abrindo o navegador')
            os.startfile('C:\\Users\\Narutinn\\AppData\\Local\\Programs\\Opera GX\\75.0.3969.279\\opera.exe', "open")

        #// Spotify
        elif self.Input in ('aplicativo verde', 'spotify'):
            resposta('abrindo o Spotify')
            os.startfile('C:\\Users\\Narutinn\\AppData\\Roaming\\Spotify\\Spotify.exe', 'open')

        #// Discord
        elif self.Input in ('aplicativo azul', 'discordia', 'discórdia'):
            resposta('abrindo o Discord')
            os.startfile('C:\\Users\\Narutinn\\AppData\\Local\\Discord\\Update.exe', 'open')

        #-= Aleatorios =-#

        #// Encerrar o assistente
        elif 'desliga' in self.Input: 
            resposta('encerrando')
            return sys.exit()

        #// Pesquisar as atividades
        elif 'procurar atividade' in self.Input: 
            atividades_base()

        #// Falar atividades
        elif 'atividades encontradas' in self.Input: 
            extract_ativi()            

        #// Encerra
        elif self.estado == False:
            sys.exit()