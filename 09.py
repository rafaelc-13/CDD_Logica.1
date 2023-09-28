'''Faça um código que receba o
número de alunos de uma sala de
aula e depois solicite as notas
desses alunos, no final, mostre a
média aritmética da turma.'''

qtd_aluno = int(input('Quantos alunos tem a sala? '))
x=1
nota_turma = 0
while x <= qtd_aluno:
    nota = float(input(f'Nota do {x}º aluno: '))
    x += 1
    nota_turma += nota
media = nota_turma/qtd_aluno
print(f'A média da turma é: {media}.')
