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

RAs_curso_problematico = []


def verificacao_imagem(RA):
    """
    Verifica se a seta para o campo complementar foi exibida.

    A ausência da seta indica que o curso não abriu corretamente. Nesse
    caso, cancela a tela atual e registra o RA como curso problemático.

    Parâmetros:
        RA: Registro Acadêmico do aluno em processamento.

    Retorno:
        True se a seta não foi encontrada; False se a tela está disponível.
    """
    coord_seta_campo_dm = pyautogui.locateOnScreen(
        r"location/06.Aba_de_ajuste_curso/seta_para_campo_complemento.png",
        grayscale=True,
        confidence=0.95,
    )

    if coord_seta_campo_dm is not None:
        return False

    cancelar = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/exception/Cancelar.png"
    )
    clicar_imagem(cancelar)

    RAs_curso_problematico.append(RA)
    return True

def filtrando_curso(RA,CaminhoImg):
    """
    Localiza e seleciona o curso técnico indicado na base.

    Usa a imagem informada para clicar somente no curso correto do RA.
    Depois valida se a tela de ajuste foi aberta antes de avançar.

    Parâmetros:
        RA: Registro Acadêmico do aluno em processamento.
        CaminhoImg: Caminho da imagem usada para localizar o curso.

    Retorno:
        True se o curso apresentou problema; False se está pronto para ajuste.
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
    Ajusta os campos complementares do curso técnico selecionado.

    Atualiza os campos de parceria, estado e instituição conforme as
    regras da crítica, confirma a alteração e finaliza a correção.
    """
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
