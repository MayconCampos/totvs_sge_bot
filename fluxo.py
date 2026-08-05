import time

import pyautogui

from funcoes import (
    apagar_texto,
    clicar_imagem,
    copiar_conteudo,
    digitar,
    ler_imagem,
    passar_campos,
    personalizar_clique,
    preencher_campo_estado,
    preencher_campo_instituicao,
    preencher_campo_parceria,
    preencher_campo_tem_parceria,
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

def filtrando_curso():
    time.sleep(0.5)
    coord_curso = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/curso_padrao.png",
        r"location/06.Aba_de_ajuste_curso/curso_padrao_logistica.png",
        r"location/06.Aba_de_ajuste_curso/curso_padrao_informatica.png",
        r"location/06.Aba_de_ajuste_curso/curso_padrao_segunraca_trabalho.png",
        r"location/06.Aba_de_ajuste_curso/curso_padrao_automacao_industrial.png",
        r"location/06.Aba_de_ajuste_curso/curso_padrao_edificacao.png",
        r"location/06.Aba_de_ajuste_curso/curso_padrao_eletrotecnica.png",
        r"location/06.Aba_de_ajuste_curso/curso_padrao_mecanica.png",
        r"location/06.Aba_de_ajuste_curso/curso_padrao_mecatronica.png",
        )
    clicar_imagem(coord_curso,2)

    # Campo Complementar - Produção DN
    time.sleep(0.5)
    coord_seta_campo_dm = ler_imagem(r"location/06.Aba_de_ajuste_curso/seta_para_campo_complemento.png")
    personalizar_clique(coord_seta_campo_dm, x_deslocamento=25, quantidade=4)

    # Produção DN
    time.sleep(0.5)
    coord_producao_dn = ler_imagem(r"location/06.Aba_de_ajuste_curso/aba_de_ajuste.png")
    clicar_imagem(coord_producao_dn, quantidade=4)

def ajuste_campo_complementar():
    #Tem parceria?
    time.sleep(0.5)
    coord_campo_parceria= ler_imagem(r"location/07.ajuste_cursos/aba_tem_parceria.png")
    personalizar_clique(coord_campo_parceria,y_deslocamento=20)
    conteudo = copiar_conteudo()
    preencher_campo_tem_parceria(conteudo)
    passar_campos(1)
    pyautogui.press("enter")

    # Campo Parceiria
    time.sleep(0.5)
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
    time.sleep(0.5)
    preencher_campo_instituicao()
    passar_campos(quantidade= 1)

    #Finalizando correção
    time.sleep(0.5)
    coord_finalizando_correcao = ler_imagem(r"location/07.ajuste_cursos/OK.png")
    clicar_imagem(coord_finalizando_correcao)

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
