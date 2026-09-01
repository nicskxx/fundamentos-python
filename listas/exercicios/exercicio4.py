def remover_produto(produtos, produto):
    produtos.remove(produto)


produtos = ["Arroz", "Feijão", "Macarrão", "Leite"]

remover_produto(produtos, "Macarrão")

print(produtos)