def verificar():
    aluno = {
        "nome": "Nicolas",
        "media": 8.0,
        "frequencia": 80
    }

    if aluno["media"] >= 6 and aluno["frequencia"] >= 75:
        print(aluno["nome"], "foi aprovado.")
    else:
        print(aluno["nome"], "foi reprovado.")

verificar()