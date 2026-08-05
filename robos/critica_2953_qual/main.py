from robos.critica_2953_qual.fluxo import executar_ajuste
from totvs.fluxo_comum import (
    anexo_do_RA,
    filtro_aluno,
    primeira_filial,
    trocar_filial,
    trocando_RA,
)


def processar_filiais(filiais_e_ras):
    """Processa pares de filial e respectivos RAs usando a navegação comum."""
    eh_primeira_filial = True

    for filial, registros_aluno in filiais_e_ras:
        primeiro_ra = True

        for ra in registros_aluno:
            if primeiro_ra:
                if eh_primeira_filial:
                    primeira_filial(filial)
                else:
                    trocar_filial(filial)

                filtro_aluno(ra)
                anexo_do_RA()
                primeiro_ra = False
            else:
                trocando_RA(ra)

            executar_ajuste()

        eh_primeira_filial = False


def executar():
    raise NotImplementedError(
        "Defina a fonte de filiais e RAs da crítica 2953 qualitativa e "
        "chame processar_filiais()."
    )


if __name__ == "__main__":
    executar()
