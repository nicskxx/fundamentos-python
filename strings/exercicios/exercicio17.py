def limpar_telefone(telefone):
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace(" ", "")
    telefone = telefone.replace("-", "")

    return telefone

print(limpar_telefone("(19) 99999-8888"))