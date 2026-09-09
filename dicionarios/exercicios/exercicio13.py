def remover():
    funcionario = {
        "nome": "Nicolas",
        "idade": 15,
        "cargo": "Estagiário",
        "salario": 1500,
        "telefone": "19999999999"
    }

    chave = input("Digite a chave que deseja remover: ")

    if chave in funcionario:
        del funcionario[chave]
        print(funcionario)
    else:
        print("Chave não encontrada.")

remover()