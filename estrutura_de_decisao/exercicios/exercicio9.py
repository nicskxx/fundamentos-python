def calculadora():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, * ou /): ")

    if operacao == "+":
        resultado = numero1 + numero2
        print("Resultado:", resultado)
    elif operacao == "-":
        resultado = numero1 - numero2
        print("Resultado:", resultado)
    elif operacao == "*":
        resultado = numero1 * numero2
        print("Resultado:", resultado)
    elif operacao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado:", resultado)
        else:
            print(f"Não é possível dividir por zero.")
    else:
        print("Operação inválida.")


calculadora()
