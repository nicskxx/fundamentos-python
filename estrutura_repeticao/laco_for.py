import time
def mostrar_numero():
    for i in range (1,6):
        print(f"o numero atual é {i}")
        time.sleep(2)
#mostrar_numero()

def mostrar_numero_alternado():
    for num in range(0,20,2):
        print(num)
        time.sleep(0.1)
#mostrar_numero_alternado()

#def somar_numeros():
    total = 0
    for valor in range(1,20):
        total += valor
    print(total)
#somar_numeros()

def mostrar_par():
    for valor in range(0,20):
        if valor % 2 == 0:
            print(valor)
        else:
            print(f"impar{valor}")
#mostrar_par()




def laco_alinhado():
    nomes = ['nicolas', 'laura', 'sohia', 'david', 'mariana', 'mayara']
    notas = [8, 9, 10]
    for nome in nomes:
        print(f'nome: {nome}')
        for nota in notas:
            print(f'nota: {notas }')
laco_alinhado()
