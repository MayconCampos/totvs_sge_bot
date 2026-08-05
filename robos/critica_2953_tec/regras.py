import pyautogui


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
