def consultar():
    cliente = {
        "nome": "Nicolas",
        "idade": 15,
        "cidade": "Piracicaba",
        "telefone": "19999999999"
    }

    informacao = input("Digite o nome da informação: ")

    resultado = cliente.get(informacao)

    if resultado is not None:
        print(resultado)
    else:
        print("Informação não encontrada.")

consultar()