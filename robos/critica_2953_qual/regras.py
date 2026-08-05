import pyautogui

def aplicar_regras(conteudo):
    if conteudo == "1" or conteudo =="0" or conteudo =="":
        pyautogui.write("0")
