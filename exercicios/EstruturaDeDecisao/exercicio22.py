# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão). 

inputDoUtilizador = int(input('digite um numero: '))

def parOuImpar(numero):
    return (numero % 2) and 'O numero é Impar.' or 'O numero é Par.'

print(parOuImpar(inputDoUtilizador));