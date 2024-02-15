# Faça um programa que leia 5 números e informe a soma e a média dos números. 

numeros = []
for i in range(5):
    numeros.append(int(input(f'Insert number {i+1}: ')))
print(f'A soma é: {sum(numeros)}')