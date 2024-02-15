# Faça um programa que peça um número inteiro e determine 
# se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1. 

# primos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

# função com recursão
def primo(numero, index = 2):
    if numero <= 1:
        return False
    if numero == index:
        return True
    if numero % index == 0:
        return False
    index += 1
    return primo(numero, index)

inputDoUtilizador = int(input('Introduza um numero inteiro: '))
print('O numero é primo.') if primo(inputDoUtilizador) else print('O numero não é primo.')