from fluxo import *

df_base_ra = pd.read_excel(r"C:\Users\manoel.campos\OneDrive - SFIEMT\Área de Trabalho\AutomatizacaoERP\Base_RAs\teste_30_07_2026_c11000h.xlsx", dtype={"RegistroAluno": str, "CodFilialSGE": str})
cod_filial_unique = df_base_ra["CodFilialSGE"].drop_duplicates().tolist()

tempo_inicial = time.time()
eh_primeira_filial = True
count = 0
total = len(df_base_ra)

for filial in cod_filial_unique:
    df_filtrada = df_base_ra[df_base_ra["CodFilialSGE"] == filial]
    #Status zero é o primeiro laço do loop
    primeiro_ra = True
       
    for RA in df_filtrada["RegistroAluno"]:
        count += 1
        print(f"Processando {count}/{total} | Filial: {filial} | RA: {RA}")

        if primeiro_ra:

            if eh_primeira_filial:
                primeira_filial(filial)
            else:
                trocar_filial(filial)

            time.sleep(0.5)
            filtro_aluno(RA)
            anexo_do_RA()

            time.sleep(0.5)
            filtrando_curso()

            time.sleep(0.5)
            ajuste_campo_complementar()
            primeiro_ra = False

        else:
            trocando_RA(RA)

            time.sleep(0.5)
            filtrando_curso()

            time.sleep(0.5)
            ajuste_campo_complementar()
        
    eh_primeira_filial = False

tempo_decorrido = time.time() - tempo_inicial
minutos = int(tempo_decorrido //60)
segundos = tempo_decorrido % 60

print(f"Tempo total: {minutos} min {segundos:.2f} s")