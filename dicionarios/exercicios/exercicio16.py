def compras():
    compra = {
        "cliente": "Nicolas",
        "produtos": []
    }

    for i in range(5):
        produto = input("Digite o nome do produto: ")
        compra["produtos"].append(produto)

    print("Cliente:", compra["cliente"])
    print("Produtos:")

    for produto in compra["produtos"]:
        print(produto)

compras()