# Faça um programa que receba dois números inteiros e gere os números inteiros
# que estão no intervalo compreendido por eles. 

numeros = ''
for i in range(int(input(f'Insert number: '))+1, int(input(f'Insert number: '))):
    numeros += (f' {i}')
print(numeros)