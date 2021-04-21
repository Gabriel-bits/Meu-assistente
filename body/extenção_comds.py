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

pygame.init()
pygame.mixer.pre_init(42050, -16, 2, 4096)

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


def music():

    pygame.mixer.init()
    mu = pygame.mixer.music.load("music/3_30 AM Eating _ Lofi Hip Hop Mix.m4a")
    mu = pygame.mixer.music.play(1)





# C:/Users/Narutinn/Music/Bot
