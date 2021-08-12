import threading
import sys
import speech_recognition as sr
import asyncio, tracemalloc, time
from PyQt5 import uic,QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
tracemalloc.start()

# -=- Foldes import -=- #

from fuct import*
from body.head import Assistent

# -=- ======+====== -=- #

Assistent = Assistent()
app = QtWidgets.QApplication([])

def encerra():
    Assistent.estado = False
    app.quit()

async def janela():
    interface = uic.loadUi('interface.ui')
    interface.pushButton.clicked.connect(encerra)
    interface.show()
    app.exec()


def inicio():

    while True:

        try:
            Assistent.comandos()
                

        except sr.UnknownValueError:
            print("\r")
            pass
            
        except Exception as er:
            resposta("ocorreu um erro senhor.")
            resposta(f"o erro foi... {er}")
            print(f"*+[ {er} ]+*")
            pass
        # Assisten.comandos()
# inicio()
threading.Thread(target=inicio).start()
asyncio.run(janela())

# threading.Thread(target=inicio, )
# asyncio.run(inicio())

