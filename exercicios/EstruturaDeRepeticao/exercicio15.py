# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo. 

def fibonacci(number):
    if number == 0: return [0]
    numeros = [0,1]
    for i in range(2, number+1):
        numeros.append(numeros[i-1]+numeros[i-2])
    return numeros

print(fibonacci(int(input('Introduza um numero: '))))