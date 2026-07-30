import pyautogui
import os
import time
import pyperclip
import pandas as pd
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent
pyautogui.FAILSAFE = True
pyautogui.useImageNotFoundException(False)

import logging
import os
import time
import pyautogui


class ImagemNaoEncontradaError(Exception):
    pass


def ler_imagem(*imagens, tempo_limite=15):

    for imagem in imagens:
        if not os.path.exists(imagem):
            mensagem = f"Arquivo de imagem inexistente: {imagem}"

            logging.error(mensagem)

            raise FileNotFoundError(mensagem)

    logging.info(f"Procurando imagem(s): {imagens}")

    tempo_inicial = time.time()

    while True:

        for imagem in imagens:

            coordenada = pyautogui.locateOnScreen(
                imagem,
                grayscale=True,
                confidence=0.95
            )

            if coordenada is not None:
                logging.info(
                    f"Imagem encontrada: {imagem} | "
                    f"Coordenada: {coordenada}"
                )

                return coordenada

        tempo_decorrido = time.time() - tempo_inicial

        if tempo_decorrido >= tempo_limite:

            os.makedirs(
                "logs/prints",
                exist_ok=True
            )

            nome_print = (
                f"logs/prints/erro_{int(time.time())}.png"
            )

            pyautogui.screenshot(nome_print)

            mensagem = (
                f"Nenhuma das imagens foi encontrada após "
                f"{tempo_limite} segundos: {imagens}. "
                f"Print salvo em: {nome_print}"
            )

            logging.error(mensagem)

            raise ImagemNaoEncontradaError(mensagem)

        time.sleep(0.2)


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

def preencher_campo_tem_parceria(conteudo):
    if conteudo == "1" or conteudo =="0":
            pyautogui.write("1")

def preencher_campo_parceria(conteudo):
    if conteudo == "" or conteudo =="0":
        pyautogui.write("0")

def preencher_campo_estado():
    pyautogui.write("MT")

def preencher_campo_instituicao():
    pyautogui.write("SEDUC")




