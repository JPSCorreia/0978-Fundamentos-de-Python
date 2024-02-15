# Classe Retangulo: Crie uma classe que modele um retangulo:

#     Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#     Métodos: Mudar valor dos lados, Retornar valor dos lados,
#     calcular Área e calcular Perímetro;
#     Crie um programa que utilize esta classe. Ele deve pedir ao usuário
#     que informe as medidades de um local. Depois, deve criar um objeto com as medidas
#     e calcular a quantidade de pisos e de rodapés necessárias para o local.


class Retangulo:

    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novoLadoA, novoLadoB):
        self.ladoA = novoLadoA
        self.ladoB = novoLadoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return self.ladoA * 2 + self.ladoB * 2

    def describe(self):
        return self.ladoA, self.ladoB


retangulo = Retangulo(
    int(input("Introduza o valor de um lado em cm: ")),
    int(input("Introduza o valor de outro lado em cm: ")),
)
print(
    f"O retangulo tem como lados {retangulo.describe()[0]}cm e {retangulo.describe()[1]}cm, a sua área é {retangulo.calcularArea()}cm e o seu perimetro é {retangulo.calcularPerimetro()}cm."
)
