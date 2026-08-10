import time

import pandas as pd

from robos.critica_2953_tec.fluxo import (
    RAs_curso_problematico,
    ajuste_campo_complementar,
    filtrando_curso,
)
from totvs.fluxo_comum import (
    anexo_do_RA,
    filtro_aluno,
    primeira_filial,
    trocar_filial,
    trocando_RA,
)


def executar_2953_tec():
    df_base_ra = pd.read_excel(r"C:\Users\manoel.campos\OneDrive - SFIEMT\Área de Trabalho\AutomatizacaoERP\Base_RAs\Novissimo_ensino_medio_c1_1000h.xlsx", dtype={"RegistroAluno": str, "CodFilialSGE": str, "CaminhoImg": str})
    cod_filial_unique = df_base_ra["CodFilialSGE"].drop_duplicates().tolist()

    tempo_inicial = time.time()
    eh_primeira_filial = True
    count = 0
    total = len(df_base_ra)

    for filial in cod_filial_unique:
        df_filtrada = df_base_ra[df_base_ra["CodFilialSGE"] == filial]
        #Status zero é o primeiro laço do loop
        primeiro_ra = True

        for RA, CaminhoImg in df_filtrada[["RegistroAluno", "CaminhoImg"]].itertuples(index=False, name=None):
            CaminhoImg = CaminhoImg.replace("\t","").strip()
            count += 1
            print(f"Processando {count}/{total} | Filial: {filial} | RA: {RA}")

            if primeiro_ra:

                if eh_primeira_filial:
                    primeira_filial(filial)
                else:
                    trocar_filial(filial)

                time.sleep(1)
                filtro_aluno(RA)
                anexo_do_RA()

                time.sleep(0.5)
                curso_problematico = filtrando_curso(RA,CaminhoImg)

                time.sleep(0.5)
                if not curso_problematico:
                    ajuste_campo_complementar()

                primeiro_ra = False

            else:
                time.sleep(1)
                trocando_RA(RA)

                time.sleep(0.5)
                curso_problematico = filtrando_curso(RA,CaminhoImg)

                time.sleep(0.5)
                if not curso_problematico:
                    ajuste_campo_complementar()

        eh_primeira_filial = False

    tempo_decorrido = time.time() - tempo_inicial
    minutos = int(tempo_decorrido //60)
    segundos = tempo_decorrido % 60

    print(f"Tempo total: {minutos} min {segundos:.2f} s")
    print(f"Lista de Ras problematicos: {RAs_curso_problematico}")

if __name__ == "__main__":
    executar_2953_tec()
