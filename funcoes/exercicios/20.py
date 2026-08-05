def cadastro():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    profissao = input("Profissão: ")
    cidade = input("Cidade: ")

    print("======= CADASTRO =======")
    print("Nome:", nome)
    print("Idade:", idade, "anos")
    print("Profissão:", profissao)
    print("Cidade:", cidade)
    print("========================")

cadastro()
