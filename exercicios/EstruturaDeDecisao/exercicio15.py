# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#     Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#     Triângulo Equilátero: três lados iguais;
#     Triângulo Isósceles: quaisquer dois lados iguais;
#     Triângulo Escaleno: três lados diferentes;

inputDoUtilizador = [
    float(input("Introduza um lado de um triângulo: ")),
    float(input("Introduza o segundo lado de um triângulo:  ")),
    float(input("Introduza o terceiro lado de um triângulo:  ")),
]


def verificarTriangulo(lados):
    return (((lados[0] + lados[1]) > lados[2]) and ((lados[0] + lados[2]) > lados[1]) and ((lados[2] + lados[1]) > lados[0]))

def determinarTipoDeTriangulo(lados):
    if (lados[0] == lados[1] == lados[2]): return 'Equilátero'
    if (lados[0] != lados[1] != lados[2]): return 'Escaleno'
    return 'Isósceles'

print(determinarTipoDeTriangulo(inputDoUtilizador) if (verificarTriangulo(inputDoUtilizador)) else 'Não é um triangulo')