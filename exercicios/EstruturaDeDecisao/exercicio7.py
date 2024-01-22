# Faça um Programa que leia três números e mostre o maior e o menor deles. 

inputDoUtilizador = [int(input('introduza um numero: ')), int(input('introduza outro numero: ')), int(input('introduza outro numero: '))]

def saberMaiorEMenor(listaDeNumeros):
    return [sorted(listaDeNumeros)[-1], sorted(listaDeNumeros)[0]]

maiorEMenor = saberMaiorEMenor(inputDoUtilizador)

print(f'o numero maior é: {maiorEMenor[0]}, o numero menor é: {maiorEMenor[1]}')    