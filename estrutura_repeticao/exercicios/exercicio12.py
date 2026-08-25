def eh_primo():
    numero = int(input("Digite um número: "))

    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


resultado = eh_primo()

if resultado == True:
    print("É primo")
else:
    print("Não é primo")
