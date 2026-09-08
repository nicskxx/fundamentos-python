import urllib

from urllib3.util import url


def separar_nome(nome_completo):
    parte = nome_completo.split()
    return parte
nome_completo = input("Informe um nome completo: ")
print(separar_nome(nome_completo))

def criar_nome_completo(partes):
    nome_completo = ','.join(partes)
    return nome_completo

partes_nome = ['Nicolas','de', 'campos', 'barboza']
print(criar_nome_completo(partes_nome))

def analisar_url():
    inicia_com_https = url.startswith('https://')
    termina_com_br = url.endswith('br')
    return inicia_com_https, termina_com_br

url = 'https://www.google.com'
print(analisar_url())


def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print('idade_valida')
    else:
        print('idade invalida')
idade = input("Informe uma idade: ")
validar_idade(idade)

def validar_Nome(nome):
    nome_valida = nome.isalpha()
    if nome_valida:
        print('nome valida')
    else:
        print('nome invalida')
