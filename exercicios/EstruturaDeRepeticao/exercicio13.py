# Faça um programa que peça dois números, base e expoente, 
# calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem. 

base = soma = int(input(f'Base: '))
for i in range(1, int(input(f'Expoente: '))):
    soma = soma*base
print(soma)