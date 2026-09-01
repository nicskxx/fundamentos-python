estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]


def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print("Produto vendido!")
    else:
        print("Produto não está disponível.")

    return estoque


estoque = vender_produto(estoque, "Mouse")

print("Estoque atualizado:", estoque)