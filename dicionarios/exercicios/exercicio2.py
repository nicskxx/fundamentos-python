def alterar():
    aluno = {
        "nome": "Nicolas",
        "idade": 15,
        "telefone": "19999999999",
        "endereco": "Rua das Flores",
        "cidade": "Piracicaba",
        "nota": 8.5,
        "turma": "DS",
        "curso": "Desenvolvimento de Sistemas"
    }

    print("Antes:")
    print(aluno)

    aluno["idade"] = 16
    aluno["cidade"] = "Campinas"

    print("Depois:")
    print(aluno)

alterar()