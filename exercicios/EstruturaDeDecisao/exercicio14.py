# Faça um programa que lê as duas notas parciais obtidas por um aluno numa 
# disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
#       Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0        A
#       Entre 7.5 e 9.0         B
#       Entre 6.0 e 7.5         C
#       Entre 4.0 e 6.0         D
#       Entre 4.0 e zero        E

# O algoritmo deve mostrar na tela as notas, 
# a média, o conceito correspondente e a mensagem “APROVADO” 
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. 

inputDoUtilizador = [float(input('introduza uma nota: ')), float(input('introduza outra nota: '))]

def calcularMedia(notas):
    return ((notas[0] + notas[1])/2)

def atribuirConceito(media):
    if ( 9.0 < media <= 10.0):
        return 'A' 
    if ( 7.5 < media <= 9.0):
        return 'B' 
    if ( 6.0 < media <= 7.5):
        return 'C'
    if ( 4.0 < media <= 6.0):
        return 'D' 
    return 'E'

print(atribuirConceito(calcularMedia(inputDoUtilizador)))