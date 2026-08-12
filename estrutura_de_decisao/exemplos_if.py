def aluno_aprovado():
    nota1 = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    media = (nota1 + nota2) / 2

    if media >= 7:
        print("aprovado")
    elif media >= 5 and media < 7:

        print("aluno  de recuperacao")
    else:
        print("reprovado")


aluno_aprovado()







