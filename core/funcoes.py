import logging
import os
import time

import pyautogui
import pyperclip


pyautogui.FAILSAFE = True
pyautogui.useImageNotFoundException(False)


class ImagemNaoEncontradaError(Exception):
    """
    Indica que nenhuma das imagens esperadas foi encontrada na tela
    dentro do tempo limite definido.
    """
    pass


def ler_imagem(*imagens, tempo_limite=15):
    """
    Procura uma ou mais imagens na tela e retorna a primeira encontrada.

    Antes da busca, valida se todos os arquivos de imagem existem. Se o
    tempo limite for atingido, salva um print da tela para diagnóstico.

    Parâmetros:
        *imagens: Caminhos das imagens que serão procuradas, em ordem.
        tempo_limite: Tempo máximo, em segundos, para localizar uma imagem.

    Retorno:
        Coordenada da primeira imagem localizada na tela.

    Exceções:
        FileNotFoundError: Quando algum arquivo de imagem não existe.
        ImagemNaoEncontradaError: Quando nenhuma imagem é localizada no prazo.
    """

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
                confidence=0.85
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
    """
    Move o mouse até o centro de uma coordenada e realiza um ou mais cliques.

    Parâmetros:
        coordenada: Posição da imagem localizada na tela.
        quantidade: Número de cliques a serem realizados.
    """
    x, y = pyautogui.center(coordenada)
    pyautogui.moveTo(x,y, duration= 0.5)
    pyautogui.click(clicks=quantidade)


def digitar(escrita):
    """
    Digita um texto no campo que está selecionado na tela.

    Parâmetros:
        escrita: Texto que será digitado.
    """
    pyautogui.write(escrita)

def personalizar_clique(coordenada, x_deslocamento = 0, y_deslocamento = 0, quantidade = 1):
    """
    Clica em uma posição relativa ao centro de uma imagem localizada.

    Permite ajustar o ponto do clique horizontalmente ou verticalmente
    quando o centro da imagem não é o local desejado.

    Parâmetros:
        coordenada: Posição da imagem localizada na tela.
        x_deslocamento: Ajuste horizontal em pixels. Positivo move à direita.
        y_deslocamento: Ajuste vertical em pixels. Positivo move para baixo.
        quantidade: Número de cliques a serem realizados.
    """

    x, y = pyautogui.center(coordenada)

    x = x + x_deslocamento
    y = y + y_deslocamento
    pyautogui.moveTo(x,y)
    pyautogui.click(clicks=quantidade)

def apagar_texto():
    """
    Seleciona todo o texto do campo ativo e o remove.
    """
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

def limpar_area_transferencia():
    """
    Remove o conteúdo atual da área de transferência.
    """
    pyperclip.copy("")

def passar_campos(quantidade):
    """
    Avança entre campos da tela usando a tecla Tab.

    Parâmetros:
        quantidade: Número de vezes que a tecla Tab será pressionada.
    """
    pyautogui.press("tab", presses=quantidade, interval=0.2)

def copiar_conteudo():
    """
    Copia o conteúdo do campo ativo para a área de transferência.

    Seleciona todo o conteúdo do campo, copia o texto e remove espaços
    extras no início e no fim antes de retorná-lo.

    Retorno:
        Texto copiado do campo ativo.
    """
    pyperclip.copy("") #limpando campo de copia
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")

    time.sleep(0.3)

    conteudo = pyperclip.paste().strip()

    return conteudo
