# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120 

def factorial(numero):
    for i in range(numero-1, 1, -1):
        numero = numero * i
    return numero

print(f"O factorial é: {factorial(int(input('Introduza um numero: ')))}")