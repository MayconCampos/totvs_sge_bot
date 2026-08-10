import pyautogui

def aplicar_regras(conteudo):
    """
    Aplica a regra de preenchimento para o campo de parceria.

    Quando o campo estiver com valor "1", "0" ou vazio, informa o valor
    "0" para atender à regra da crítica.

    Parâmetros:
        conteudo: Valor atual copiado do campo "Tem parceria?".
    """
    if conteudo == "1" or conteudo =="0" or conteudo =="":
        pyautogui.write("0")
