def prestacao():
    valor = float(input("Valor do produto: "))
    parcelas = int(input("Quantidade de parcelas: "))

    valor_parcela = valor / parcelas

    print("Valor de cada parcela:", valor_parcela)

prestacao()
