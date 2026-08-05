def comissao():
    salario_fixo = float(input("Salário fixo: "))
    vendas = float(input("Valor das vendas: "))
    percentual = float(input("Percentual de comissão: "))

    salario_final = salario_fixo + (vendas * percentual / 100)

    print("Salário final:", salario_final)

comissao()
