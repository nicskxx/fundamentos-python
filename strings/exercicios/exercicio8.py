def verificar_palavra(texto, palavra):
    if palavra in texto:
        print("Palavra encontrada!")
    else:
        print("Palavra não encontrada!")

verificar_palavra("Nicolas gosta de Python", "Python")