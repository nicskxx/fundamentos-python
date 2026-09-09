def adicionar():
    pessoa = {
        "nome": "Nicolas",
        "idade": 15
    }

    pessoa["email"] = input("Digite o email: ")
    pessoa["endereco"] = input("Digite o endereço: ")
    pessoa["telefone"] = input("Digite o telefone: ")

    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("Email:", pessoa["email"])
    print("Endereço:", pessoa["endereco"])
    print("Telefone:", pessoa["telefone"])

adicionar()