def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    return posicao


produtos = ["Arroz", "Feijão", "Macarrão", "Leite"]

posicao = encontrar_produto(produtos, "Macarrão")

print(posicao)