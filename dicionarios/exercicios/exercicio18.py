produtos = []


def cadastrar():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    estoque = int(input("Digite o estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    print("Produto cadastrado.")


def listar():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print("Nome:", produto["nome"])
            print("Preço: R$", produto["preco"])
            print("Estoque:", produto["estoque"])
            print()


def buscar():
    nome = input("Digite o nome do produto: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print("Nome:", produto["nome"])
            print("Preço: R$", produto["preco"])
            print("Estoque:", produto["estoque"])
            return

    print("Produto não encontrado.")


def atualizar():
    nome = input("Digite o nome do produto: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            quantidade = int(input("Digite a quantidade: "))

            produto["estoque"] += quantidade

            if produto["estoque"] < 0:
                produto["estoque"] = 0

            print("Estoque atualizado.")
            print("Estoque atual:", produto["estoque"])
            return

    print("Produto não encontrado.")


def remover():
    nome = input("Digite o nome do produto: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            print("Produto removido.")
            return

    print("Produto não encontrado.")


def sistema():
    while True:
        print("===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar estoque")
        print("5 - Remover produto")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            atualizar()
        elif opcao == "5":
            remover()
        elif opcao == "6":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


sistema()