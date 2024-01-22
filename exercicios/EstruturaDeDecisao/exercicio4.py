# Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

vogais = { 'a', 'e', 'i', 'o', 'u'}
inputDoUtilizador = ''

while (not inputDoUtilizador.isalpha()):
    inputDoUtilizador = input('Introduza uma letra: ')

def vogalOuConsoante(letra):
    if letra in vogais: 
        return 'vogal'
    return 'consoante'

print(vogalOuConsoante(inputDoUtilizador))