notas = [7.5, 6.0, 8.5, 9.0, 5.5]

def adicionar_nota(notas, nota):
    notas.append(nota)

def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)

def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)

def remover_nota(notas, nota):
    notas.remove(nota)

def remover_ultima_nota(notas):
    return notas.pop()

def encontrar_nota(notas, nota):
    return notas.index(nota)

def quantidade_notas(notas):
    return len(notas)

def ordenar_notas(notas):
    return sorted(notas)

def inverter_notas(notas):
    return list(reversed(notas))

def soma_notas(notas):
    return sum(notas)

def media_notas(notas):
    return sum(notas) / len(notas)


print("Notas iniciais:", notas)

adicionar_nota(notas, 10.0)
print("Depois de adicionar:", notas)

inserir_nota(notas, 7.0, 2)
print("Depois de inserir:", notas)

adicionar_varias_notas(notas, [6.5, 8.0])
print("Depois de adicionar várias:", notas)

remover_nota(notas, 5.5)
print("Depois de remover:", notas)

ultima = remover_ultima_nota(notas)
print("Última nota removida:", ultima)
print("Notas atuais:", notas)

posicao = encontrar_nota(notas, 8.5)
print("Posição da nota 8.5:", posicao)

print("Quantidade de notas:", quantidade_notas(notas))

print("Notas ordenadas:", ordenar_notas(notas))

print("Notas invertidas:", inverter_notas(notas))

print("Soma das notas:", soma_notas(notas))

print("Média da turma:", media_notas(notas))