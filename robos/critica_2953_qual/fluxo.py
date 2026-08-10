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
    """
    Verifica se ocorreu erro ao abrir o curso selecionado.

    Ao identificar a mensagem de erro, confirma o aviso, fecha a tela
    do curso e registra o RA na lista de cursos problemáticos.

    Parâmetros:
        RA: Registro Acadêmico do aluno em processamento.

    Retorno:
        True se o curso apresentou erro; False se não houve erro.
    """
    time.sleep(3)

    coord_erro = pyautogui.locateOnScreen(
        r"location/06.Aba_de_ajuste_curso/exception/Erro.png",
        grayscale=True,
        confidence=0.95,
    )

    if coord_erro is None:
        return False

    coord_erro = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/exception/OK_inicial.png",
    )
    clicar_imagem(coord_erro)

    coord_sair_curso = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/exception/Cancelar.png"
    )
    clicar_imagem(coord_sair_curso)

    RAs_curso_problematico.append(RA)
    return True

def filtrando_curso(RA,CaminhoImg):
    """
    Localiza e seleciona o curso específico que será tratado.

    Usa o caminho da imagem informado pela base para clicar somente no
    curso correto do RA. Se não houver erro, abre a aba de ajuste.

    Parâmetros:
        RA: Registro Acadêmico do aluno em processamento.
        CaminhoImg: Caminho da imagem usada para localizar o curso.

    Retorno:
        True se o curso apresentou erro; False se está disponível para ajuste.
    """
    curso_especifco = ler_imagem(CaminhoImg)
    clicar_imagem(curso_especifco,2)

    time.sleep(1.5)
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
    """
    Ajusta o campo complementar do curso selecionado.

    Verifica o valor do campo "Tem parceria?", aplica a regra da crítica,
    confirma a alteração e finaliza a correção na tela.
    """
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
