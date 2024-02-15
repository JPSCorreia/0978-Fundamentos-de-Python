# Faça um programa que peça 10 números inteiros, calcule e mostre 
# a quantidade de números pares e a quantidade de números impares.

# for i in range(1, 11):
#     if (int(input('Introduza um numero: ')) % 2 == 0): 
#         pares = 1 if 'pares' not in locals() else pares + 1
# print(f'Nº pares: {pares}, Nº impares: {10-pares}')

# pares = 0
# for i in range(1, 5):
#     if ( int(input('Introduza um numero: ')) % 2 == 0): pares += 1
# print(f'Nº pares: {pares}, Nº impares: {10-pares})

for i in range(1, 11):
    if (int(input('Introduza um numero: ')) % 2 == 0): 
        try: pares += 1
        except NameError: pares = 1
print(f'Nº pares: {pares}, Nº impares: {10-pares}')

