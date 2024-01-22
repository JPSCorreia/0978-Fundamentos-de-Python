# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

numNotas = 4
soma = 0
for x in range(numNotas):
    nota = int(input('digite um nota: '))
    soma = soma + nota
print(soma/numNotas)
