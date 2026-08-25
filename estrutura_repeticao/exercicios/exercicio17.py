def jogo_adivinhacao():
    numero_secreto = 10

    acertou = False

    while acertou == False:
        numero = int(input("Digite seu palpite: "))

        if numero == numero_secreto:
            print("Você acertou!")
            acertou = True

        elif numero < numero_secreto:
            print("O número secreto é maior.")

        else:
            print("O número secreto é menor.")


jogo_adivinhacao()
