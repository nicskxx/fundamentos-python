def calcular_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = peso / (altura ** 2)

    print("Seu IMC é:", round(imc, 2))

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc <= 24.9:
        print("Peso normal")
    elif imc <= 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")


calcular_imc()
