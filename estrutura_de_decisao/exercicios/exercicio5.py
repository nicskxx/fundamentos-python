def classificar_nota():
    nota = float(input("Digite uma nota de 0 a 10: "))

    if nota >= 0 and nota <= 4:
        print("Insuficiente")
    elif nota <= 6:
        print("Regular")
    elif nota <= 8:
        print("Bom")
    elif nota <= 10:
        print("Excelente")
    else:
        print("Nota inválida.")


classificar_nota()
