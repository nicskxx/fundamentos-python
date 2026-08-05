def energia():
    consumo = float(input("Consumo em kWh: "))
    preco = float(input("Preço do kWh: "))

    conta = consumo * preco

    print("Valor da conta:", conta)

energia()
