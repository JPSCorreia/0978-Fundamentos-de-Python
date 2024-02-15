# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
#     Possua uma classe chamada Ponto, com os atributos x e y.
#     Possua uma classe chamada Retangulo, com os atributos largura e altura.
#     Possua uma função para imprimir os valores da classe Ponto
#     Possua uma função para encontrar o centro de um Retângulo.
#     Você deve criar alguns objetos da classe Retangulo.
#     Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
#     A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
#     O valor do centro do objeto deve ser mostrado na tela
#     Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo. 

class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Ponto com coordenadas {self.x} x e {self.y} y.'
    


class Retangulo:
    
    def __init__(self, largura, altura, verticePartida):
        self.largura = largura
        self.altura = altura
        self.verticePartida = verticePartida
    
    def __str__(self):
        return f'Retangulo com largura {self.largura} e altura {self.altura}.'
    
    def acharCentro(self):
        return (self.largura + self.verticePartida.x)/2, (self.altura + self.verticePartida.y)/2
        
    def alterarLarguraEAltura(self, novaLargura, novaAltura):
        self.largura = novaLargura
        self.altura = novaAltura
        self.acharCentro()


retangulo1 = Retangulo(5, 10, Ponto(-1, -1))
print(f'Centro do rectangulo: {retangulo1.acharCentro()}')
retangulo1.alterarLarguraEAltura(10,20)
print(f'Centro do rectangulo: {retangulo1.acharCentro()}')
