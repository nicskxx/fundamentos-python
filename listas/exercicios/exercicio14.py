def adicionar_produtos(compras, produtos):
    compras.extend(produtos)


def cancelar_compra(compras, produto):
    compras.remove(produto)


compras = ["Arroz", "Feijão"]

produtos = ["Leite", "Pão", "Café"]

adicionar_produtos(compras, produtos)

print("Lista de compras:", compras)

cancelar_compra(compras, "Pão")

print("Após cancelar:", compras)