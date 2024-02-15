# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500. 

def fibonacci():
    numeros = [0,1]
    i = 1
    while True:
        if (numeros[i] > 500): return numeros
        i += 1
        numeros.append(numeros[i-1]+numeros[i-2])

print(fibonacci())

# import sys

# def fibonacci():
#     numeros = [0,1]
#     for i in range(2, sys.maxsize):
#         numeros.append(numeros[i-1]+numeros[i-2])
#         if (numeros[i] > 500): return numeros

# print(fibonacci())

# from itertools import count

# def fibonacci():
#     numeros = [0,1]
#     for i in count(start=2):
#         numeros.append(numeros[i-1]+numeros[i-2])
#         if (numeros[i] > 500): return numeros

# print(fibonacci())

