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

def filtrando_curso():
    time.sleep(0.5)
    coord_curso = ler_imagem(
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao.png",
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao_logistica.png",
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao_informatica.png",
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao_segunraca_trabalho.png",
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao_automacao_industrial.png",
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao_edificacao.png",
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao_eletrotecnica.png",
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao_mecanica.png",
        r"location/06.Aba_de_ajuste_curso/2953_tec/curso_padrao_mecatronica.png",
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
