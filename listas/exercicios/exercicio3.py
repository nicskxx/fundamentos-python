def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)


convidados = ["João", "Maria"]

novos_convidados = ["Pedro", "Nicolas", "Ana"]

adicionar_convidados(convidados, novos_convidados)

print(convidados)