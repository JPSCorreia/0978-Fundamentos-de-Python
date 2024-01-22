# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9). 

grausEmFahrenheit = float(input('introduza os graus em Fahrenheit: '))
grausEmCelsius = 5*((grausEmFahrenheit-32) / 9)
print(f'Graus Celsius: {round(grausEmCelsius, 1):g} ºC')
