def login():
    usuario = {
        "usuario": "Nicolas",
        "senha": "1234"
    }

    nome = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if nome == usuario["usuario"] and senha == usuario["senha"]:
        print("Login realizado com sucesso.")
    else:
        print("Usuário ou senha incorretos.")

login()