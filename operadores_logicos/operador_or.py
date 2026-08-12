# operador or
def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input("digite tem dinheiro? "))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"usuario pode comprar? {autorizado}")

posso_comprar()