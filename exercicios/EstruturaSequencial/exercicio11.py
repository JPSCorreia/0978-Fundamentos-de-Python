# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo. 

numero1 = int(input('digite um numero inteiro: '))
numero2 = int(input('digite outro numero inteiro: '))
numero3 = float(input('digite um numero real: '))
print(f'o produto do dobro do primeiro com metade do segundo: {(numero1*2)*(numero2/2):g}')
print(f'a soma do triplo do primeiro com o terceiro: {(numero1*3)+numero3:g}')
print(f'o terceiro elevado ao cubo: {numero3**3:g}')