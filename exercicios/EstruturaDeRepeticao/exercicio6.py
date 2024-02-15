# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro. 

numeros = ''
for i in range(1, 21):
    numeros += (f' {i}')
print(numeros)

numeros2 = []
for i in range(1, 21):
    numeros2.append(i)
print(numeros2)