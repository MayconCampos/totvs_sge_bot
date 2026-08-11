from robos.critica_2953_tec.main import executar_2953_tec
from robos.critica_2953_Qualificacao_Aprendizagem.main import executar_2953_qualificacao_aprendizagem
    
def menu():
    print("Escolha o robô:")
    print("1 - Crítica 2953 Técnico")
    print("2 - Crítica 2953 ajuste para Qualificação ou Aprendizagem")

    opcao = input("Opção: ")

    if opcao == "1":
        executar_2953_tec()
    elif opcao == "2":
        executar_2953_qualificacao_aprendizagem()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    menu()
