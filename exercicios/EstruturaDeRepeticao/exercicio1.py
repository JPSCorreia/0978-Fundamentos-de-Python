# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

nota = -1
while ((nota < 0) or (nota > 10)):
    nota = int(input('Introduza uma nota entre 0 e 10: '))
    if ((nota < 0) or (nota > 10)): print('Nota inválida')
print('Valor válido.')