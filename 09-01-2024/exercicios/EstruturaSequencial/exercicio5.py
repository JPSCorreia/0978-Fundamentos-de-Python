# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#libraries
import math

raio = int(input('introduza um numero em metros: '))
area = round(math.pi*(raio**2), 2)
print(f'a area é: {area} m²')

