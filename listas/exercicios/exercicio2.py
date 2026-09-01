def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)


alunos = ["João", "Maria", "Pedro"]

inserir_aluno(alunos, "Nicolas", 1)

print(alunos)