import pyautogui
import os
import time
import pyperclip

pyautogui.FAILSAFE = True
pyautogui.useImageNotFoundException(False)

'''
grayscale - Faz com que a comparação de imagens seja feita em tons de cinza, ignorando as cores.
confidence - Define o quanto a imagem encontrada precisa ser parecida com a imagem de referência.
'''
'''
#No meu computador o RGE não é um executavel - .rdp (Conexão de Área de Trabalho Remota).
os.startfile(r
"C:\\Users\\manoel.campos\\OneDrive - SFIEMT\\Área de Trabalho\\SGE PROD 1.rdp")
time.sleep(1)
# #entrar no SGE
# while not pyautogui.locateOnScreen(r"location/inicio.png", grayscale = True, confidence = 0.8):
#     time.sleep(1)


#ENTRAR NO RDP DA TOTV's

# Selecionando "Unidade"
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/01.Conexao_RDP/menu_inicial_1.png", grayscale = True, confidence = 0.8)
    time.sleep(1)
pyautogui.click(pyautogui.center(encontrou))

# Selecionando "Area de transferência"
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/01.Conexao_RDP/menu_inicial_2.png", grayscale = True, confidence = 0.8)
    time.sleep(1)
pyautogui.click(pyautogui.center(encontrou))

#Passando pela primeira janela de conexão do TOTV's
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/01.Conexao_RDP/primeira_janela_conectar.png", grayscale = True, confidence = 0.8)
    time.sleep(1)
pyautogui.click(pyautogui.center(encontrou))

# PASSANDO SENHA DO WINDOWNS

# achando o campo de senha e escrevendo a senha
time.sleep(2)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/02.Senha_windows/campo_senha_1.png", grayscale = True, confidence = 0.8)
    time.sleep(1)

#Move o mouse até o centro da imagem
x, y = pyautogui.center(encontrou)

x_campo = x + 120
y_campo = y + 35

pyautogui.moveTo(x_campo, y_campo)
time.sleep(1)

pyautogui.click()
time.sleep(1)

pyautogui.write("TESTE", interval=0.2)

#confirmando 
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/02.Senha_windows/confirmacao_senha.png", grayscale = True, confidence = 0.8)
    time.sleep(1)
pyautogui.click(pyautogui.center(encontrou))
'''

# LOGIN NA TOTVs
# achando o campo de senha e escrevendo a senha

time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/03.Login_TOTVS/campo_senha.png", grayscale = True, confidence = 0.8)

x, y = pyautogui.center(encontrou)
pyautogui.moveTo(x,y)
time.sleep(1)


x_campo = x + 30

pyautogui.moveTo(x_campo, y)
time.sleep(1)

pyautogui.click(x_campo, y)
time.sleep(1)

senha = "123456789"
pyautogui.typewrite(senha)

#Confirmar senha
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/03.Login_TOTVS/confirmar_senha.png", grayscale = True, confidence = 0.8)

pyautogui.click(pyautogui.click(pyautogui.center(encontrou)))


#PESQUISANDO ALUNO
#Selecionando filtro

time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/04.Procurar_aluno/Alunos_icone.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

pyautogui.moveTo(x,y)
pyautogui.click()

#Escolhendo o modo de filtro RA

encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/04.Procurar_aluno/RA_pesquisa_aluno.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

pyautogui.moveTo(x,y)
pyautogui.click()

#Confirmação - EXECUTAR
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/04.Procurar_aluno/executar.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

pyautogui.moveTo(x,y)
pyautogui.click()


#Encontrando o campo de escrita e colocando o RA da vez
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/04.Procurar_aluno/campo_pesquisa_RA.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

pyautogui.moveTo(x,y )
pyautogui.click()
pyautogui.write("00648470")


#Confirmação - OK
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/04.Procurar_aluno/OK.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

pyautogui.moveTo(x,y)
pyautogui.click()

# CURSO ALUNO
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/05.Curso/selecionando_aluno.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

x_campo = x + 30
y_campo = y + 30
pyautogui.moveTo(x_campo,y_campo)
pyautogui.click()

#Selecionando anexo
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/05.Curso/anexo_curso.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

x_campo = x + 40

pyautogui.moveTo(x_campo,y)
pyautogui.click()

#Selecionando o curso
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/05.Curso/curso_habilitacao.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)
pyautogui.moveTo(x,y)
pyautogui.click()

#CURSO

# Selecionando curso - ADMINISTRAÇÃO
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/06.Aba_de_ajuste_curso/curso_padrao.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)
pyautogui.moveTo(x,y)
pyautogui.doubleClick()

# Indo para aba de "Campos complementares - produção DN"
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/06.Aba_de_ajuste_curso/seta_para_campo_complemento.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

x_campo = x + 25
pyautogui.moveTo(x_campo,y)
pyautogui.doubleClick()
pyautogui.doubleClick()

#Entrando na Aba de Produção DN
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/06.Aba_de_ajuste_curso/aba_de_ajuste.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)
pyautogui.moveTo(x,y)
pyautogui.click()

# AJUSTE DO CURSO

#Ajustando Parceria
time.sleep(1)
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/07_ajuste_cursos/aba_parceria.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)

y_campo = y + 20
pyautogui.moveTo(x,y_campo)
pyautogui.click()

#Verificando se o campo está vazio:
pyperclip.copy("") #limpando campo de copia
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl","c")
conteudo = pyperclip.paste().strip()


if  conteudo == "":
    pyautogui.write("0")

pyautogui.press(["tab","tab","tab"])


#Campo estado:
pyperclip.copy("") #limpando campo de copia
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl","c")
conteudo = pyperclip.paste().strip()
time.sleep(1)

if  conteudo in ["","0"]:
    pyautogui.write("MT")

time.sleep(0.3)
pyautogui.press(["tab","tab","tab","tab"])

#Campo Instituição:

pyautogui.write("SEDUC")
pyautogui.press("tab")

#Salvando os dados atualizado do curso
encontrou = None
while encontrou is None:
    encontrou = pyautogui.locateOnScreen(r"location/07_ajuste_cursos/OK.png", grayscale = True, confidence = 0.8)
x, y = pyautogui.center(encontrou)
pyautogui.moveTo(x,y)
pyautogui.click()