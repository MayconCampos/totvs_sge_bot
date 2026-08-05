from robos.critica_2953_tec.main import executar_2953_tec
from robos.critica_2953_qual.main import executar_2953_qual
    
def menu():
    print("Escolha o robô:")
    print("1 - Crítica 2953 Técnico")
    print("2 - Crítica 2953 Qualificação")

    opcao = input("Opção: ")

    if opcao == "1":
        executar_2953_tec()
    elif opcao == "2":
        executar_2953_qual()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    menu()
