# Faça um Programa que leia três números e mostre-os em ordem decrescente. 

inputDoUtilizador = [int(input('introduza um numero: ')), int(input('introduza outro numero: ')), int(input('introduza outro numero: '))]

def ordenarDecrescentemente(listaDeNumeros):
    return sorted(listaDeNumeros, reverse=True)

numerosEmOrdemDecrescente = ordenarDecrescentemente(inputDoUtilizador)

print('Numeros por ordem decrescente:')    
for numero in numerosEmOrdemDecrescente:
    print(numero)
