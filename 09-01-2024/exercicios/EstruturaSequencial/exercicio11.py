# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('introduza a sua altura: '))
pesoIdeal = (72.7*altura) - 58
print(f'{pesoIdeal:g} kg')

