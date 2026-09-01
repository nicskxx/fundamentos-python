def criar_ranking(pontuacoes):
    return sorted(pontuacoes, reverse=True)


pontuacoes = [150, 320, 90, 450, 280]

ranking = criar_ranking(pontuacoes)

print(ranking)