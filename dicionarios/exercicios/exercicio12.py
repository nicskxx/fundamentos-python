def remover():
    funcionario = {
        "nome": "Nicolas",
        "idade": 15,
        "cargo": "Estagiário",
        "salario": 1500,
        "telefone": "19999999999"
    }

    print("Antes da remoção:")
    print(funcionario)

    telefone = funcionario.pop("telefone")

    print("Telefone removido:", telefone)

    print("Depois da remoção:")
    print(funcionario)

remover()