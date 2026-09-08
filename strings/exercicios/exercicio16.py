def verificar_extensao(nome_arquivo):
    if nome_arquivo.endswith(".pdf"):
        print("Arquivo válido.")
    else:
        print("Arquivo inválido.")

verificar_extensao("nicolas.pdf")