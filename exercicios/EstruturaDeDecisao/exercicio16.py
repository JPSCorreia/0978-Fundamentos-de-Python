# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
# informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
# e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

inputDoUtilizador = [
    float(input("introduza o valor de a: ")),
    float(input("introduza o valor de b: ")),
    float(input("introduza o valor de c: ")),
]


def verificarSegundoGrau(valores):
    return True if valores[0] else False


def calcularDelta(valores):
    return (valores[1] ** 2) - (4 * valores[0] * valores[2])


def funcaoSegundoGrau(valores, delta):
    raizes = ""
    if (delta < 0): raizes = "A equação não possui uma raiz real."
    if (delta >= 0): raizes = f"Raiz: {(-valores[1] + math.sqrt(delta))/(2 * valores[0]):g}"
    if (delta > 0): raizes = raizes + f" e Raiz: {(-valores[1] - math.sqrt(delta))/(2 * valores[0]):g}"
    return raizes


print(
    funcaoSegundoGrau(inputDoUtilizador, calcularDelta(inputDoUtilizador)) if verificarSegundoGrau(inputDoUtilizador) else "Equação não é de segundo grau."
)