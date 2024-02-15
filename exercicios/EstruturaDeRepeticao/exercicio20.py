# Altere o programa de cálculo do fatorial, permitindo ao usuário 
# calcular o fatorial 
# várias vezes e limitando o fatorial a 
# números inteiros positivos e menores que 16. 

def factorial(numero):
    for i in range(numero-1, 1, -1):
        numero = numero * i
    return numero

keepRunning = 's'
while (keepRunning == 's'):
    inputDoUtilizador = 0
    while(inputDoUtilizador > 15 or inputDoUtilizador < 1):
        inputDoUtilizador = int(input('Introduza um numero: '))
    print(f"O factorial é: {factorial(inputDoUtilizador)}")
    keepRunning = input('Deseja continuar a correr o programa? (s se sim): ')