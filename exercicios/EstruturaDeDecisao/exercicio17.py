# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 
inputDoUtilizador = int(input("introduza um ano: "))

def verificarSeBissexto(ano):
    return not (ano % 4)

print('Ano bissexto' if verificarSeBissexto(inputDoUtilizador) else 'Ano não bissexto')
