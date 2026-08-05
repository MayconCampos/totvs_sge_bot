import time

import pyautogui

from core.funcoes import (
    clicar_imagem,
    copiar_conteudo,
    ler_imagem,
    passar_campos,
    personalizar_clique,
)
from robos.critica_2953_qual.regras import (
    aplicar_regras
)


def filtrando_curso():
    time.sleep(0.5)
    coord_curso = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/2953_qual/ASSISTENTE ADMINISTRATIVO COM INFORMÁTICA.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/ASSISTENTE CONTÁBIL FINANCEIRO.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/ASSISTENTE DE CONTROLE DA QUALIDADE.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/ASSISTENTE DE RECURSOS HUMANOS COM INFORMÁTICA.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/ASSISTENTE DE RECURSOS HUMANOS.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/ELETRICISTA DE INSTALAÇÕES PREDIAIS .png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/ELETRICISTA INDUSTRIAL.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/OPERADOR DE COMPUTADOR.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/OPERADOR DE EMPILHADEIRA.png",
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
    aplicar_regras(conteudo)
    passar_campos(1)
    pyautogui.press("enter")

    time.sleep(0.5)
    coord_finalizando_correcao = ler_imagem(r"location/07.ajuste_cursos/OK.png")
    clicar_imagem(coord_finalizando_correcao)
