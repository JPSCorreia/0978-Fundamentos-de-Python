# Faça um programa que calcule o mostre a média aritmética de N notas. 

def media(notas):
    return sum(notas)/len(notas)

# testes:
print(f'A média é: {media([10, 15, 20, 10, 12])}')
print(f'A média é: {media([9, 17, 20, 20, 12, 20, 19, 18, 13, 20])}')
