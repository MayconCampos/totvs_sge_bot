import pyautogui


def preencher_campo_tem_parceria(conteudo):
    """
    Aplica a regra para o campo "Tem parceria?".

    Quando o campo contém "1" ou "0", informa o valor "1".

    Parâmetros:
        conteudo: Valor atual copiado do campo.
    """
    if conteudo in ("","0","1"):
            pyautogui.write("1")

def preencher_campo_parceria(conteudo):
    """
    Aplica a regra para o campo de parceria.

    Quando o campo está vazio ou contém "0", informa o valor "0".

    Parâmetros:
        conteudo: Valor atual copiado do campo.
    """
    if conteudo == "" or conteudo =="0":
        pyautogui.write("0")

def preencher_campo_estado():
    """
    Preenche o campo de estado com a sigla MT.
    """
    pyautogui.write("MT")

def preencher_campo_instituicao():
    """
    Preenche o campo de instituição com SEDUC.
    """
    pyautogui.write("410")
