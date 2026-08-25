def contar_pares():
    inicio = int(input("Digite o início: "))
    fim = int(input("Digite o fim: "))

    quantidade = 0

    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            quantidade = quantidade + 1

    return quantidade


resultado = contar_pares()

print("Quantidade de números pares:", resultado)
