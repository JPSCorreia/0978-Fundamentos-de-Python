# Altere o programa de cálculo dos números primos, informando, 
# caso o número não seja primo, por quais número ele é divisível. 

# função com recursão

def primo(numero, index = 2):
    if numero <= 1:
        print(f'Lista de divisores: {1}')
        return False
    if numero == index:
        return True
    if numero % index == 0:
        divisores = []
        for j in range(numero, 0, -1):
            if(numero % j == 0): divisores.append(j)
        print(f'Lista de divisores: {divisores}')
        return False
    index += 1
    return primo(numero, index)

inputDoUtilizador = int(input('Introduza um numero inteiro: '))
print('O numero é primo.') if primo(inputDoUtilizador) else print('O numero não é primo.')