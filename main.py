from fluxo import *

df_base_ra = pd.read_excel(r"C:\Users\manoel.campos\OneDrive - SFIEMT\Área de Trabalho\AutomatizacaoERP\Base_RAs\022__alunos_com_informacao_de_parceria_2026-07-27T16_00_39.4344432-04_00.xlsx", dtype={"RegistroAluno": str, "CodFilialSGE": str})
cod_filial_unique = df_base_ra["CodFilialSGE"].drop_duplicates().tolist()

eh_primeira_filial = True
for filial in cod_filial_unique:
    df_filtrada = df_base_ra[df_base_ra["CodFilialSGE"] == filial]
    #Status zero é o primeiro laço do loop
    primeiro_ra = True
       
    for RA in df_filtrada ["RegistroAluno"]:
        if primeiro_ra:

            if eh_primeira_filial == False:
                trocar_filial(filial)

            primeira_filial(filial)

            time.sleep(1)
            filtro_aluno(RA)
            anexo_do_RA()

            time.sleep(1)
            filtrando_curso()

            time.sleep(1)
            ajuste_campo_complementar()
            primeiro_ra = False

    else:
            trocando_RA(RA)
            time.sleep(1)

            filtrando_curso()
            time.sleep(1)

            ajuste_campo_complementar()
    eh_primeira_filial = False