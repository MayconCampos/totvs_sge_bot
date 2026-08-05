import time

import pyautogui

from core.funcoes import (
    apagar_texto,
    clicar_imagem,
    digitar,
    ler_imagem,
    personalizar_clique,
)


def trocar_filial(filial):
    coord_troca_unidade = ler_imagem(r"location/09.Troca_Unidade/troca_de_unidade.png")
    personalizar_clique(coord_troca_unidade,x_deslocamento = 15, quantidade=1)
    time.sleep(0.5)

    pyautogui.hotkey("alt", "tab")
    pyautogui.hotkey("alt", "tab")
    #acaba não usando o botão YES e confirma a troca no "enter"
    #coord_confirmar_fechamento = ler_imagem(r"location/09.Troca_Unidade/YES.png")
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

def primeira_filial(filial):
    coord_troca_unidade = ler_imagem(r"location/09.Troca_Unidade/troca_de_unidade.png")
    personalizar_clique(coord_troca_unidade,x_deslocamento = 15, quantidade=1)
    time.sleep(0.5)

    coord_filtro_unidade = ler_imagem(r"location/09.Troca_Unidade/campo_filial.png")
    personalizar_clique(coord_filtro_unidade, y_deslocamento=15, quantidade=1)
    apagar_texto()
    digitar(filial)

    time.sleep(0.5)
    coord_concluir = ler_imagem(r"location/09.Troca_Unidade/CONCLUIR.png")
    clicar_imagem(coord_concluir)


def filtro_aluno(RA):
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

def anexo_do_RA():
    # Entrando em curso/habilitção
    time.sleep(0.5)
    coord_anexo_filtro = ler_imagem(r"location/05.Curso/anexo_curso.png")
    personalizar_clique(coord_anexo_filtro,x_deslocamento = 40)

    #Entrando em cursos habilitação
    time.sleep(0.5)
    coord_curso_habilitacao = ler_imagem(r"location/05.Curso/curso_habilitacao.png")
    clicar_imagem(coord_curso_habilitacao,1)

def trocando_RA(RA):
    #Selecionar o filtro de pesquisa
    time.sleep(0.5)
    coord_filtro_RA = ler_imagem(r"location/08.segundo_loop/filtro_RA_direto.png")
    clicar_imagem(coord_filtro_RA,1)

    #Clicar no campo de texto do filtro
    time.sleep(0.5)
    coord_campo_pesquisa = ler_imagem(r"location/08.segundo_loop/pesquisa_RA.png")
    personalizar_clique(coord_campo_pesquisa,y_deslocamento=20,quantidade=2)

    #Apagar RA antigo
    apagar_texto()

    #Digitar o RA
    digitar(RA)

    #Confirmar pesquisa
    coord_confirmar_filtro = ler_imagem(r"location/08.segundo_loop/OK.png")
    clicar_imagem(coord_confirmar_filtro,1)
    time.sleep(0.5)
