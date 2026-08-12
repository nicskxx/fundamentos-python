def calcular_frete():
    valor = float(input("Digite o valor da compra: "))

    if valor <= 100:
        frete = 20
    elif valor <= 300:
        frete = 10
    else:
        frete = 0

    valor_final = valor + frete

    print("Frete: R$", frete)
    print("Valor total: R$", valor_final)


calcular_frete()
