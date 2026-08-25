def calcular_media():
    soma = 0
    quantidade = 0

    numero = float(input("Digite um número ou 0 para parar: "))

    while numero != 0:
        soma = soma + numero
        quantidade = quantidade + 1

        numero = float(input("Digite um número ou 0 para parar: "))

    if quantidade > 0:
        media = soma / quantidade
        print("A média é:", media)
    else:
        print("Nenhum número foi informado.")


calcular_media()
