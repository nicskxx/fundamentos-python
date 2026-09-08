# converter texto para maiusculas e minusculas.
def formatar_nome(nome):
    nome_maiusculo = nome.upper()
    nome_minusculo = nome.lower()

    nome_camelcase = nome_maiusculo.capitalize()

    return nome_maiusculo, nome_minusculo, nome_camelcase

nome = input("Informe o nome do aluno: ")


nome_maiusculo, nome_minusculo , nome_camelcase = formatar_nome(nome)

print(nome_maiusculo)
print(nome_minusculo)
print(nome_camelcase)

#remover espaços desnecessarios

def limpar_texto(texto):
    texto = texto.strip()

    #.lstrip
    #.rstrip


    return texto

texto_1 = ("    paython é legal        ")
print(texto_1)

print(limpar_texto(texto_1))

def trocar_cidade(cidade,):
    texto_trocado = cidade.replace(cidade, "Piracicaba")
    return texto_trocado

cidade = "eu moro em Piracicaba"
print(trocar_cidade(cidade))


def analisar_texto(texto, letra):
    qtde_caracteres = len(texto)

    qtde_letra = texto.strip().lower().count(letra)
    return  qtde_caracteres , qtde_letra


texto_2 = input("Informe o texto: ")
letra = input("Informe uma letra: ")
caracteres, letra = analisar_texto(texto_2, letra)
print(f'quantiedade de caracteres {caracteres}')
print(f'quantidade de letras : {letra}')


def verificar_palavra(frase,palavra):
    palavra_presente = palavra.lower() in frase.lower()
    return palavra_presente

frase = input("Informe uma frase: ")
palavra = input("Informe uma palavra: ")

print(f"a palavra está presente na frase {verificar_palavra(frase,palavra )}")


def encontrar_posicao_palavra(frase,palavra):
    posicao_palavra = frase.lower().find(palavra.lower())
    return posicao_palavra
frase_2 = input("Informe uma frase: ")
palavra_2 = input("Informe uma palavra: ")

print(f'a posição da palavra é {encontrar_posicao_palavra(frase_2,palavra_2)})')