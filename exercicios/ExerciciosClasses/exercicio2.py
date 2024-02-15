# Classe Quadrado: Crie uma classe que modele um quadrado:

#     Atributos: Tamanho do lado
#     Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novoLado):
        self.lado = novoLado

    def calcularArea(self):
        print(self.lado * self.lado)

quadrado1 = Quadrado(4)
quadrado1.calcularArea()
quadrado1.mudarLado(5)
quadrado1.calcularArea()
