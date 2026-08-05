def consumo():
    distancia = float(input("Distância percorrida: "))
    combustivel = float(input("Quantidade de combustível: "))

    consumo_medio = distancia / combustivel

    print("Consumo médio:", consumo_medio, "km/L")

consumo()
