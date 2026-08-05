def exibir_mensagem():
    print('hello world')

exibir_mensagem()


def soma():
    valor1 = 50
    valor2 = 20
    total = valor1 + valor2
    print(f'A soma vale {total}')

soma()

def subtracao():
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    total = valor1 - valor2
    print(f'A subtração vale {total}')

subtracao()

def media():
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    media = (valor1 + valor2) / 2
    return media
nota_final = media()
print(nota_final)