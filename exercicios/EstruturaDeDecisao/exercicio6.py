# Faça um Programa que leia três números e mostre o maior deles. 
inputDoUtilizador = [int(input('introduza um numero: ')), int(input('introduza outro numero: ')), int(input('introduza outro numero: '))]

def saberMaior(listaDeNumeros):
    return sorted(listaDeNumeros)[-1]

print(f'o numero maior é: {saberMaior(inputDoUtilizador)}')    