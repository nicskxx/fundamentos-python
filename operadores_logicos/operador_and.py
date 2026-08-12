#operador and
from operator import and_


def pode_dirigir():
    idade = int(input("Digite sua idade: "))
    CARTA = True

    autorizado = idade >= 18 and CARTA
    print(f"usuario pode dirigir? {autorizado}")

pode_dirigir()