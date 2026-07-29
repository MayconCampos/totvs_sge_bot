import pyautogui
import os
import time
import pyperclip
import pandas as pd
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent
pyautogui.FAILSAFE = True
pyautogui.useImageNotFoundException(False)

def ler_imagem(imagem):
    coordenada = None
    while coordenada is None:
        coordenada = pyautogui.locateOnScreen(
            imagem, 
            grayscale = True, 
            confidence = 0.8)
    return coordenada


def clicar_imagem(coordenada,quantidade = 1):
    x, y = pyautogui.center(coordenada)
    pyautogui.moveTo(x,y, duration= 0.5)
    pyautogui.click(clicks=quantidade)


def digitar(escrita):
    pyautogui.write(escrita)

def personalizar_clique(coordenada, x_deslocamento = 0, y_deslocamento = 0, quantidade = 1):
    """
    x - horizontal = -----
                   
    y - Vertical = |

    numero positvo = desce
    numero negativo = sobe
    """

    x, y = pyautogui.center(coordenada)

    x = x + x_deslocamento
    y = y + y_deslocamento
    pyautogui.moveTo(x,y)
    pyautogui.click(clicks=quantidade)

def apagar_texto():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

def limpar_area_transferencia():
    pyperclip.copy("")

def passar_campos(quantidade):
    pyautogui.press("tab", presses=quantidade, interval=0.2)

def copiar_conteudo():
    pyperclip.copy("") #limpando campo de copia
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")

    time.sleep(0.3)

    conteudo = pyperclip.paste().strip()

    return conteudo

def preencher_campo_parceria(conteudo):
    if conteudo == "" or conteudo =="0":
        pyautogui.write("0")

def preencher_campo_estado():
    pyautogui.write("MT")

def preencher_campo_instituicao():
    pyautogui.write("SEDUC")




