# exercicio combinado

def posso_entrar_veigh():
    POSSUI_INGRESSO = True
    idade = int(input("digite sua idade: "))
    nome_na_lista = bool(input(" seu esta nome_na_lista? "))

    posso_entra = idade >= 18 and (nome_na_lista or POSSUI_INGRESSO)

    print(f"vou entrar {posso_entra}")

posso_entrar_veigh()