def classificar_temperatura():
    temperatura = float(input("Digite a temperatura em Celsius: "))

    if temperatura < 15:
        print("Frio")
    elif temperatura <= 25:
        print("Agradável")
    else:
        print("Quente")


classificar_temperatura()
