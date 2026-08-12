




def login():
    email = "Nicolas@gmail.com"

    senha = "1234"
    codigo_secreto = "#456@"

    email_input = input("Digite o seu e-mail: ")
    senha_input = input("Digite sua senha: ")

    if email_input == email and senha_input == senha:
        print(f"Usuário logado!")
        acessar_admin = input("Deseja acessar area administrativa? (Digite S ou N) ")
        if acessar_admin == "S":
           codigo_secreto_input = input("Digite o código secreto: ")
           if codigo_secreto_input == codigo_secreto:
                print("Acesso admin liberado!")
           else:
                print("Código incorreto!")
        elif acessar_admin == "N":
              print("Ok. Você acessou como usuário comum")
        else:
            print("Opção inválida!")
    else:
        print("Email ou senha incorreto(a)!")

login()