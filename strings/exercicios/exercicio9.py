def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

print(contar_palavras("Nicolas gosta muito de Python"))