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
    caminho_imagem = PASTA_PROJETO / imagem

    print(f"Buscando arquivo em: {caminho_imagem}")

    coordenada = None

    while coordenada is None:
        coordenada = pyautogui.locateOnScreen(
            str(caminho_imagem),
            grayscale=True,
            confidence=0.8
        )

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

'''
#ABRINDO O SISTEMA DA TOTVS

coord_campo_senha = ler_imagem(r"location/03.Login_TOTVS/campo_senha.png")
clicar_imagem(coord_campo_senha,1)
digitar("123456789")
coord_entrar_tots = ler_imagem(r"location/03.Login_TOTVS/confirmar_senha.png")
clicar_imagem(coord_entrar_tots,1)
pyperclip.copy("")
'''
time.sleep(2)
# time.sleep(30)
df_base_ra = pd.read_excel(r"C:\Users\manoel.campos\Desktop\AutomatizacaoERP\totvs_sge_bot\Base_RAs\022__alunos_com_informacao_de_parceria_2026-07-27T16_00_39.4344432-04_00.xlsx", dtype={"RegistroAluno": str, "CodFilialSGE": str})
cod_filial_unique = df_base_ra["CodFilialSGE"].drop_duplicates().tolist()

primeira_filial = True
for filial in cod_filial_unique:

    df_filtrada = df_base_ra[df_base_ra["CodFilialSGE"] == filial]
    #Status zero é o primeiro laço do loop
    primeiro_ra = True
   
    for RA in df_filtrada ["RegistroAluno"]:
        if primeiro_ra:
            #TROCANDO UNIDADE DO SGE
            #Selecionando Unidade:
            coord_troca_unidade = ler_imagem(r"location/09.Troca_Unidade/troca_de_unidade.png")
            personalizar_clique(coord_troca_unidade,x_deslocamento = 15, quantidade=1)
            time.sleep(2)

            if primeira_filial == False:
                pyautogui.hotkey("alt", "tab")
                pyautogui.hotkey("alt", "tab")
                coord_confirmar_fechamento = ler_imagem(r"location/09.Troca_Unidade/YES.png")
                pyautogui.press("enter")


            #Filtrando Unidade através do codigo unidade
            coord_filtro_unidade = ler_imagem(r"location/09.Troca_Unidade/campo_filial.png")
            personalizar_clique(coord_filtro_unidade, y_deslocamento=15, quantidade=1)
            apagar_texto()
            digitar(filial)
            time.sleep(0.5)

            #Confirmando filial
            coord_concluir = ler_imagem(r"location/09.Troca_Unidade/CONCLUIR.png")
            clicar_imagem(coord_concluir)

            #PROCESSO DE FILTRO RA
            #Abrindo o Filtro - Aluno RA
            time.sleep(0.5)
            coord_filtro_Ra = ler_imagem(r"location/04.Procurar_aluno/Alunos_icone.png")
            clicar_imagem(coord_filtro_Ra,1)

            #Escolhendo o tipo RA
            time.sleep(0.5)
            coord_tipo_RA = ler_imagem(r"location/04.Procurar_aluno/RA_pesquisa_aluno.png")
            clicar_imagem(coord_tipo_RA,1)

            #Botão executar
            time.sleep(0.5)
            coord_confirmando_escolha = ler_imagem(r"location/04.Procurar_aluno/executar.png")
            clicar_imagem(coord_confirmando_escolha,1)

            # Digitando RA do aluno
            time.sleep(0.5)
            coord_campo_pesquisa = ler_imagem(r"location/04.Procurar_aluno/campo_pesquisa_RA.png")
            clicar_imagem(coord_campo_pesquisa,1)
            pyautogui.write(RA)
            # digitar("00648280")

            time.sleep(0.5)
            coord_confirma_pesquisa = ler_imagem(r"location/04.Procurar_aluno/OK.png")
            clicar_imagem(coord_confirma_pesquisa,1)


            # ENTRANDO EM CURSOS/HABILITAÇÃO

            # Anexo
            time.sleep(0.5)
            coord_anexo_filtro = ler_imagem(r"location/05.Curso/anexo_curso.png")
            personalizar_clique(coord_anexo_filtro,x_deslocamento = 40)

            #Entrando em cursos habilitação
            time.sleep(0.5)
            coord_curso_habilitacao = ler_imagem(r"location/05.Curso/curso_habilitacao.png")
            clicar_imagem(coord_curso_habilitacao,1)


            # TRATAMENTO DA CRITICA

            #Selecionando Administração
            time.sleep(0.5)
            coord_curso = ler_imagem(r"location/06.Aba_de_ajuste_curso/curso_padrao.png")
            clicar_imagem(coord_curso,2)

            # Campo Complementar - Produção DN
            time.sleep(0.5)
            coord_seta_campo_dm = ler_imagem(r"location/06.Aba_de_ajuste_curso/seta_para_campo_complemento.png")
            personalizar_clique(coord_seta_campo_dm, x_deslocamento=25, quantidade=4)

            # Produção DN
            time.sleep(0.5)
            coord_producao_dn = ler_imagem(r"location/06.Aba_de_ajuste_curso/aba_de_ajuste.png")
            clicar_imagem(coord_producao_dn, quantidade=4)


            ## AJUSTANDO O CURSO

            # Campo Parceria
            time.sleep(1)
            coord_campo_parceria= ler_imagem(r"location/07.ajuste_cursos/aba_parceria.png")
            personalizar_clique(coord_campo_parceria,y_deslocamento=20)
            conteudo = copiar_conteudo()
            preencher_campo_parceria(conteudo)
            passar_campos(quantidade= 3)

            # Campo Estado
            time.sleep(1)
            preencher_campo_estado()
            passar_campos(quantidade= 4)

            #Campo instituição
            time.sleep(1)
            preencher_campo_instituicao()
            passar_campos(quantidade= 1)

            #Finalizando correção
            time.sleep(1)
            coord_finalizando_correcao = ler_imagem(r"location/07.ajuste_cursos/OK.png")
            clicar_imagem(coord_finalizando_correcao)
            primeiro_ra = False

            time.sleep(3)
        else:
            #Selcionar o filtro de pesquisa
            coord_filtro_RA = ler_imagem(r"location/08.segundo_loop/filtro_RA_direto.png")
            clicar_imagem(coord_filtro_RA,1)

            #Clicar no campo de texto do filtro
            coord_campo_pesquisa = ler_imagem(r"location/08.segundo_loop/pesquisa_RA.png")
            personalizar_clique(coord_campo_pesquisa,y_deslocamento=20,quantidade=2)

            #Apagar RA antigo
            apagar_texto()

            #Digitar o RA
            digitar(RA)
            
            #Confirmar pesquisa
            coord_confirmar_filtro = ler_imagem(r"location/08.segundo_loop/OK.png")
            clicar_imagem(coord_confirmar_filtro,1)
            time.sleep(2)

            # TRATAMENTO DA CRITICA
            #Selecionando Administração
            time.sleep(0.5)
            coord_curso = ler_imagem(r"location/06.Aba_de_ajuste_curso/curso_padrao.png")
            clicar_imagem(coord_curso,2)

            # Campo Complementar - Produção DN
            time.sleep(0.5)
            coord_seta_campo_dm = ler_imagem(r"location/06.Aba_de_ajuste_curso/seta_para_campo_complemento.png")
            personalizar_clique(coord_seta_campo_dm, x_deslocamento=25, quantidade=4)

            # Produção DN
            time.sleep(0.5)
            coord_producao_dn = ler_imagem(r"location/06.Aba_de_ajuste_curso/aba_de_ajuste.png")
            clicar_imagem(coord_producao_dn, quantidade=4)


            # AJUSTANDO O CURSO

            # Campo Parceria
            time.sleep(0.5)
            coord_campo_parceria= ler_imagem(r"location/07.ajuste_cursos/aba_parceria.png")
            personalizar_clique(coord_campo_parceria,y_deslocamento=20)
            conteudo = copiar_conteudo()
            preencher_campo_parceria(conteudo)
            passar_campos(quantidade= 3)

            # Campo Estado
            time.sleep(0.5)
            preencher_campo_estado()
            passar_campos(quantidade= 4)

            #Campo instituição
            time.sleep(0.5)
            preencher_campo_instituicao()
            passar_campos(quantidade= 1)

            #Finalizando correção
            time.sleep(0.5)
            coord_finalizando_correcao = ler_imagem(r"location/07.ajuste_cursos/OK.png")
            clicar_imagem(coord_finalizando_correcao,1)
            status = True
            time.sleep(3)
    primeira_filial = False
