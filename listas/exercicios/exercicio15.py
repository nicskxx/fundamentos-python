def adicionar_nota(notas, nota):
    notas.append(nota)


def remover_nota(notas, nota):
    notas.remove(nota)


def media_notas(notas):
    return sum(notas) / len(notas)


notas = [7, 8, 9]

adicionar_nota(notas, 10)

print("Notas:", notas)

remover_nota(notas, 8)

print("Notas após remover:", notas)

media = media_notas(notas)

print("Média:", media)