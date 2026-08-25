def somar_pares():
    inicio = int(input("Digite o início: "))
    fim = int(input("Digite o fim: "))

    soma = 0

    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            soma = soma + i

    return soma


resultado = somar_pares()

print("A soma dos números pares é:", resultado)
