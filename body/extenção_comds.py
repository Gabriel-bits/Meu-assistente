import pygame
from pygame.locals import*
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as Bfs
import os, json, asyncio, time, sys
import requests, html5lib
import pandas as pd
import playsound
import random

try:
    from fuct import*
except:
    pass

def brawser():
    optios = Options()
    optios.add_argument('--headless')
    drive = webdriver.Chrome(executable_path="C:/Users/Narutinn/Documents/chromedriver_win32/chromedriver.exe",options=optios)
    return drive

# pygame.init()
# pygame.mixer.pre_init(42050, -16, 2, 4096)
loca_m = 'C:/Users/Narutinn/Music/Bot/'

def atividades_base():
    conta = secret()
    optios = Options()
    # optios.add_argument('--headless')
    drive = webdriver.Chrome(executable_path="C:/Users/Narutinn/Documents/chromedriver_win32/chromedriver.exe")
    drive.get("https://classroom.google.com/u/0/h")
    drive.minimize_window()
    time.sleep(1)

    # logar no seu gmail ou étc...
    drive.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(f"{conta['gmail']}" + Keys.ENTER)
    drive.maximize_window()
    time.sleep(2)

    # sua senha
    drive.minimize_window()
    drive.find_element_by_xpath("""/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input""").send_keys(f"{conta['senha']}" + Keys.ENTER)
    drive.maximize_window()
    drive.minimize_window()
    time.sleep(13)

    atividades = {
        "nome":None,
        "data":None
    }

    data = []
    drive.maximize_window()
    drive.minimize_window()
    for datas in drive.find_elements_by_class_name("oBSRLe"):
        datas_str = datas.text
        data.append(datas_str)
        print(datas_str)
        print(len(data))

    ind = 0

    # -=- resposta pra dizer que estar em andamento
    resposta('exercícios encntrados')

    for clases in drive.find_elements_by_class_name('hrUpcomingAssignmentGroup'):
        # data = drive.find_elements_by_class_name("oBSRLe")
        ativi = clases.find_element_by_tag_name('a')
        print(ind)
        data_ind = data[ind]
        nome_ = ativi.text
        atividades.update({"nome" : ativi.text})
        atividades.update({"data" : data_ind})
        print(atividades["data"])

        time.sleep(1)
        # with open(f"assets/atividade - {ind}.json", "w") as f:
        #     json.dump(atividades, f)

        salvar_ativi(ind, atividades)

        time.sleep(1)
        print(atividades["nome"])
        ind += 1

        
    drive.quit()


def extract_ativi():
    
    for root, folder_names, file_names in os.walk("assets/"):
        nomes = file_names
        index = len(nomes)
    n = 1
    for x in nomes:
        with open(f"assets/{x}", "r") as f:
            ativi = json.load(f)
            resposta(f'atividade {n}.')
            resposta(f"{ativi['nome']}")
            resposta(f"{ativi['data']}")
        n += 1

def escam_music(dire):
    """
    Escania as musicas
    """
    n = 0
    loca_m = 'C:/Users/Narutinn/Music/Bot/'
    for root, folder, filer_names in os.walk(loca_m + dire):
        list_musicas = filer_names
    print(list_musicas)
    print(n)
    n += len(list_musicas)
    return list_musicas, n

def music_lo_fi():
    pygame.mixer.init()

    lista_de_musica, n = escam_music("lo fi/")
    print(lista_de_musica)


    playlist1 = list()
    playlist1.append('C:/Users/Narutinn/Music/Bot/lo fi/Medikit.wav')   #path to sound file
    playlist1.append('C:/Users/Narutinn/Music/Bot/lo fi/A Praça é Nossa - Música Tema.mp3')
    playlist1.append('C:/Users/Narutinn/Music/Bot/lo fi/blind.mp3')


    pygame.mixer.music.load(playlist1.pop())
    pygame.mixer.music.queue(playlist1.pop())
    print(playlist1)
    
    pygame.mixer.music.play()
    # while True:
    # for song in lista_de_musica:
    #     print(str(song))
    #     # pygame.mixer.music.load("C:/Users/Narutinn/Music/Bot/lo fi/" + str(lista_de_musica[n]))
        
    #     n -= 1
    #     pygame.mixer.music.queue(f"C:/Users/Narutinn/Music/Bot/lo fi/" + str(lista_de_musica[n]))   
    #     print(n)


    #m = pygame.mixer.music.queue("C:/Users/Narutinn/Music/Bot/lo fi/Alignment.mp3")   
    
def music_rock():
    pygame.mixer.init()
    mu = pygame.mixer.music.load(f"{loca_m}rock/")
    mu = pygame.mixer.music.play(1)

def music_ale():

    pygame.mixer.init()
    mu = pygame.mixer.music.load(f"{loca_m}ale/")
    mu = pygame.mixer.music.play(1)

def music_ambie():

    pygame.mixer.init()
    mu = pygame.mixer.music.load(f"{loca_m}ambiente/")
    mu = pygame.mixer.music.play(1)


#=-=======================================================================================================================-=#

class Music_on_():

    def __init__(self):

        optios = Options()
        optios.add_argument('--headless')
        self.drive = webdriver.Chrome(executable_path="C:/Users/Narutinn/Documents/chromedriver_win32/chromedriver.exe",options=optios)

    def music_lo_fi_on(self):
        
        # drive = brawser()
        self.drive.get("https://www.youtube.com/playlist?list=PLk5YoXhDDcAaJj83iI6YbgGjFem-J8fYl")
        time.sleep(2)
        self.drive.find_element_by_xpath("""//*[@id="items"]/ytd-playlist-sidebar-primary-info-renderer/ytd-playlist-thumbnail""").click()
        time.sleep(8)
        self.drive.find_element_by_class_name('ytp-ad-skip-button').click()
        # drive.find_element_by_id('ad-text:7').click()

    def music_rock_on():
        
        drive = brawser()
        drive.get("https://youtube.com/playlist?list=PLk5YoXhDDcAZWxiX9ZJ8az-jpBZ-PB8MU")
        time.sleep(2)
        drive.find_element_by_xpath("""//*[@id="items"]/ytd-playlist-sidebar-primary-info-renderer/ytd-playlist-thumbnail""").click()
        time.sleep(8)
        drive.find_element_by_class_name('ytp-ad-skip-button').click()

    def music_ale_on():
        
        drive = brawser()
        drive.get("https://youtube.com/playlist?list=PLk5YoXhDDcAamIqdQoMXIUyCqa91Z3L-9")
        time.sleep(2)
        drive.find_element_by_xpath("""//*[@id="items"]/ytd-playlist-sidebar-primary-info-renderer/ytd-playlist-thumbnail""").click()
        time.sleep(8)
        drive.find_element_by_class_name('ytp-ad-skip-button').click()

    def music_ambiente_on():
        
        drive = brawser()
        drive.get("https://youtube.com/playlist?list=PLk5YoXhDDcAYC-LjueGVJrW8O5EoACKfQ")
        time.sleep(2)
        drive.find_element_by_xpath("""//*[@id="items"]/ytd-playlist-sidebar-primary-info-renderer/ytd-playlist-thumbnail""").click()
        time.sleep(8)
        drive.find_element_by_class_name('ytp-ad-skip-button').click()

    def parar_musica(self):
        # drive = brawser()
        self.drive.quit()
    



if __name__ == "__main__":
    music_lo_fi_on()

    while True:
        1


# C:/Users/Narutinn/Music/Bot
