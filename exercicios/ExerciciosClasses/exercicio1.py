# Classe Bola: Crie uma classe que modele uma bola:

#     Atributos: Cor, circunferencia, material
#     Métodos: trocaCor e mostraCor


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        print(self.cor)

    def describe(self):
        print(
            f"Uma bola de cor {self.cor} com {self.circunferencia}mm de circunferência e feita de {self.material}"
        )

bola1 = Bola('Vermelha', 50, 'Plastico')
bola2 = Bola('Verde', 100, 'Vidro')

bola1.mostraCor()
bola2.describe()