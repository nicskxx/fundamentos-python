def mostrar_impares():
    numero = int(input("Digite um número: "))

    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i)


mostrar_impares()
