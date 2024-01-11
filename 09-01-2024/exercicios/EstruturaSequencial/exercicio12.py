# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#     Para homens: (72.7*h) - 58
#     Para mulheres: (62.1*h) - 44.7 

sexo = ''

while ((sexo != 'M') and (sexo != 'H')):
    sexo = input('introduza se é homem(H) ou mulher(M): ')
    print((sexo != 'M'))
    
altura = float(input('introduza a sua altura: '))

if (sexo == 'H'): pesoIdeal = (72.7*altura) - 58
if (sexo == 'M'): pesoIdeal = (62.1*altura) - 44.7
print(f'{pesoIdeal:g} kg')

