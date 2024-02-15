# Faça um programa que mostre todos os primos entre 1 e N 
# sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões 
# que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e 
# o número de testes (divisões) executados. 

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

def listarPrimos(inputDoUtilizador):
    primos = []
    for numero in range(1, inputDoUtilizador+1):
        if primo(numero): primos.append(numero)
    print(f'Numeros primos: {primos}')

listarPrimos(int(input('Introduza um numero inteiro: ')))