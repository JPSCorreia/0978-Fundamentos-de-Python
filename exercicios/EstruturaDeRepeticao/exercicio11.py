# Altere o programa anterior para mostrar no final a soma dos números. 

numeros = ''
soma = 0
for i in range(int(input(f'Insert number: '))+1, int(input(f'Insert number: '))):
    numeros += (f' {i}')
    soma += i
print(f'o intervalo é:{numeros}')
print(f'A soma é: {soma}')
