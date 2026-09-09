from calculadora import *

def executar_xalculadora():

    operacoes = {
        "1":somar,
        "2":subtrair,
        "3":multiplicar,
        "4":dividir
    }

    while True:
        print("-----------CALCULADORA------------\n")
        print("=======ESCOLHA UMA OPÇAO=========")
        print("[1] Somar\n")
        print("[2] Subtrair\n")
        print("[3] Multiplicar\n")
        print("[4] Dividir\n")
        print("[0] Sair\n")

        opcao = input("escolha uma opcao")

        if opcao == '0':
            print("operacao cancelada")
            break
        if opcao not in operacoes:
            print("operacao invalida")
            continue

        numero1 = float(input("digite o primeiro valor"))
        numer2 = float(input("digite o segundo valor"))

        operacao = operacoes[opcao]

        resultado = operacao(numero1, numer2)

        print(resultado)

executar_xalculadora()