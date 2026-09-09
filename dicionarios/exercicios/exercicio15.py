def filme():
    filme = {
        "titulo": "Vingadores",
        "ano": 2019,
        "genero": "Ação",
        "notas": []
    }

    for i in range(5):
        nota = float(input("Digite uma nota: "))
        filme["notas"].append(nota)

    media = sum(filme["notas"]) / len(filme["notas"])

    print("Título:", filme["titulo"])
    print("Ano:", filme["ano"])
    print("Gênero:", filme["genero"])
    print("Notas:", filme["notas"])
    print("Média:", media)

filme()