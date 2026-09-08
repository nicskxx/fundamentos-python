def procurar_palavra(texto, palavra):
    posicao = texto.find(palavra)

    if posicao == -1:
        print("Palavra não existe no texto.")
    else:
        print("A palavra começa na posição:", posicao)

procurar_palavra("Nicolas gosta de Python", "Python")