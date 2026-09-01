def atender_cliente(fila):
    cliente = fila.pop(0)
    return cliente


fila = ["João", "Maria", "Pedro", "Ana"]

cliente_atendido = atender_cliente(fila)

print("Cliente atendido:", cliente_atendido)
print("Fila restante:", fila)