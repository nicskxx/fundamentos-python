def verificar():
    usuario = {
        "nome": "Nicolas",
        "idade": 15,
        "email": "nicolas@email.com",
        "cidade": "Piracicaba"
    }

    chave = input("Digite o nome da chave: ")

    if chave in usuario:
        print("A chave existe.")
    else:
        print("A chave não existe.")

verificar()