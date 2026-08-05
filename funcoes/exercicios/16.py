def imc():
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))

    imc = peso / (altura ** 2)

    print("IMC:", imc)

imc()
