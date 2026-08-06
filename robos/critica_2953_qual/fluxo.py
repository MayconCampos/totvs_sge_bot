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


RAs_curso_problematico = []


def verificacao_imagem(RA):
    time.sleep(0.5)

    coord_erro = pyautogui.locateOnScreen(
        r"location/06.Aba_de_ajuste_curso/exception/exception_2953_qual/Erro.png",
        grayscale=True,
        confidence=0.95,
    )

    if coord_erro is None:
        return False

    coord_erro = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/exception/exception_2953_qual/OK_inicial.png",
    )
    clicar_imagem(coord_erro)

    coord_sair_curso = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/exception/exception_2953_qual/Cancelar.png"
    )
    clicar_imagem(coord_sair_curso)

    RAs_curso_problematico.append(RA)
    return True


def filtrando_curso(RA):
    time.sleep(0.5)
    coord_curso = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/2953_qual/assentador_de_revestimentos_ceramicos.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/assistente_administrativo.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/assistente_administrativo_com_informatica.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/assistente_contabil_financeiro.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/assistente_de_controle_da_qualidade.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/assistente_de_controle_de_qualidade_com_informatica.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/assistente_de_logistica.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/assistente_de_recursos_humanos.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/assistente_de_recursos_humanos_com_informatica.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/construtor_de_alvenaria.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/cozinheiro_industrial.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/eletricista_de_instalacoes_prediais.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/eletricista_industrial.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/instalador_hidraulico.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/mecanico_de_manutencao_de_maquinas_agricolas.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/montador_e_reparador_de_computadores.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/operador_de_computador.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/operador_de_empilhadeira.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/operador_de_retroescavadeira.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/pintor_de_obras_imobiliarias.png",
        r"location/06.Aba_de_ajuste_curso/2953_qual/torneiro_mecanico.png",
        )
    clicar_imagem(coord_curso,2)

    curso_problematico = verificacao_imagem(RA)

    if curso_problematico:
        return True

    # Campo Complementar - Produção DN
    time.sleep(0.5)
    coord_seta_campo_dm = ler_imagem(r"location/06.Aba_de_ajuste_curso/seta_para_campo_complemento.png")
    personalizar_clique(coord_seta_campo_dm, x_deslocamento=25, quantidade=4)

    # Produção DN
    time.sleep(0.5)
    coord_producao_dn = ler_imagem(r"location/06.Aba_de_ajuste_curso/aba_de_ajuste.png")
    clicar_imagem(coord_producao_dn, quantidade=4)

    return False

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
