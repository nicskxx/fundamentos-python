def criar_email(nome, sobrenome, dominio):
    return nome.lower() + "." + sobrenome.lower() + "@" + dominio

print(criar_email("Nicolas", "Barboza", "exemplo.com"))