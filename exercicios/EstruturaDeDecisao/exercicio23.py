# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento. 

inputDoUtilizador = float(input('digite um numero: '))

def inteiroOuDecimal(numero):
    return (numero % 1) and 'O numero é decimal' or 'O numero é inteiro'

print(inteiroOuDecimal(inputDoUtilizador));