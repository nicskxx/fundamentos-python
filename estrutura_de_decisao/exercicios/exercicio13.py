def calcular_ingresso():
    idade = int(input("Digite a idade do cliente: "))

    if idade <= 5:
        print("Ingresso gratuito")
    elif idade <= 12:
        print("Preço do ingresso: R$ 10,00")
    elif idade <= 59:
        print("Preço do ingresso: R$ 20,00")
    else:
        print("Preço do ingresso: R$ 10,00")


calcular_ingresso()
