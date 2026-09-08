def validar_especie(animal):
    if animal.isalpha():
        print("Espécie de animal válida.")
    else:
        print("Espécie inválida.")

validar_especie("Gato")