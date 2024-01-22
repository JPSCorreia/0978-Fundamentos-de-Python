# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

inputDoUtilizador = int(input('digite um numero: '))

def positivoOuNegativo(numero):
    return (numero == 0) and ('O numero é zero') or (numero != 0) and (f'o numero é: {(numero > 0) and "positivo" or "negativo"}')

print(positivoOuNegativo(inputDoUtilizador));