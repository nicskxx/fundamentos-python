



def mostrar_numero_while():
    contador = 0
    while contador <=10:
        contador += 1
        print(f'contagem atual : {contador}')
#mostrar_numero_while()


def contagem_regressiva():
    valor_contagem = int(input('Digite o valor da contagem:maior que 10 '))
    if valor_contagem < 10:
        print('valor da contagem excedente')
    else:
        while valor_contagem >= 1:
            print(f'contagem regressiva : {valor_contagem}')
            valor_contagem -= 1
#contagem_regressiva()

def soma_finita():
    while True:
        numo1 = int(input('Digite o numero  1 : '))
        numo2 = int(input('Digite o numero  2 : '))
        if numo1 ==0:
            break
     soma = numo1 + numo2:

        print(soma)

#soma_finita()