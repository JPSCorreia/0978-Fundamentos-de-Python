# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = ((C / 5)*9) + 32.

grausEmCelsius = float(input('introduza os graus em Celsius: '))
grausEmFahrenheit = ((grausEmCelsius / 5) * 9) + 32
print(f'Graus Fahrenheit: {round(grausEmFahrenheit, 1):g} ºF')

