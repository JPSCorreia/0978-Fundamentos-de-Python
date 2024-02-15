# Faça um programa que leia 5 números e informe o maior número. 

numeros = []
for i in range(5):
    numeros.append(int(input(f'Insert number {i+1}: ')))
numeros.sort(reverse=True)
print(f'O numero maior é: {numeros[0]})