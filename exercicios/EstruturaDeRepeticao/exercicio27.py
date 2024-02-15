# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.


def pedirNumeroTurmasEAlunos():
    numAlunos = 0
    while (numAlunos > 40 or numAlunos < 1):
        numAlunos = int( input("Introduza o numero total de alunos: "))
    numTurmas = int(input("Introduza o numero de turmas: "))
    return numTurmas, numAlunos


def mediaDeAlunosPorTurma(NumeroDeTurmasEAlunos):
    numeroDeTurmas, numeroDeAlunos = NumeroDeTurmasEAlunos
    return numeroDeAlunos / numeroDeTurmas


print(f'{mediaDeAlunosPorTurma(pedirNumeroTurmasEAlunos()):g}')