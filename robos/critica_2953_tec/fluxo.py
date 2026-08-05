import time

import pyautogui

from core.funcoes import (
    clicar_imagem,
    copiar_conteudo,
    ler_imagem,
    passar_campos,
    personalizar_clique,
)
from robos.critica_2953_tec.regras import (
    preencher_campo_estado,
    preencher_campo_instituicao,
    preencher_campo_parceria,
    preencher_campo_tem_parceria,
)


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
