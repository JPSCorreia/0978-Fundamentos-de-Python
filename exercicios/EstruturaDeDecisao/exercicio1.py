# Faça um Programa que peça dois números e imprima o maior deles. 

inputDoUtilizador1, inputDoUtilizador2 = int(input('introduza um numero: ')), int(input('introduza outro numero: '))

def saberMaior(numero1, numero2):
    return (numero1 > numero2) and numero1 or numero2

print(f'o numero maior é: {saberMaior(inputDoUtilizador1, inputDoUtilizador2)}')    