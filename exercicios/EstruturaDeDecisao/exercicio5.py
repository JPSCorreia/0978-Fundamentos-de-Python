# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez. 

inputDoUtilizador1, inputDoUtilizador2 = round(float(input('Introduza uma nota: '))), round(float(input('Introduza outra nota: ')))

def calcularMedia(nota1, nota2):
    return ((nota1 + nota2) / 2)

def aprovadoOuReprovado(media):
    if (media == 10): return 'Aprovado com Distinção'
    if (media >= 7): return 'Aprovado'
    return 'Reprovado'

print(aprovadoOuReprovado(calcularMedia(inputDoUtilizador1, inputDoUtilizador2)))