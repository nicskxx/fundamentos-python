def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    ordenadas = sorted(temperaturas)

    return quantidade, soma, media, ordenadas


temperaturas = [25, 18, 30, 22, 27]

resultado = analisar_temperaturas(temperaturas)

print("Quantidade:", resultado[0])
print("Soma:", resultado[1])
print("Média:", resultado[2])
print("Temperaturas ordenadas:", resultado[3])