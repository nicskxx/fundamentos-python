def desconto():
    preco = float(input("Preço do produto: "))
    percentual = float(input("Percentual de desconto: "))

    valor_final = preco - (preco * percentual / 100)

    print("Valor final:", valor_final)

desconto()
