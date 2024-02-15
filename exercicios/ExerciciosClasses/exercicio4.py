# Classe Pessoa: Crie uma classe que modele uma pessoa:

#     Atributos: nome, idade, peso e altura
#     Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.


class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        if self.idade < 21:
            # situação 1:
            # tem 15 mas so quer crescer 2 ou seja ate 17
            # 2 anos * 0.5 = 1cm
            # situação 2:
            # tem 17 mas quer crescer 20 ou seja ate 37
            # so vai poder crescer 4 if self.idade + anos > 21 entao fazer self.crescer(0.5 * (21 - self.idade))
            # 2 anos * 0.5 = 1cm (so quer crescer ate 19)
            if (self.idade + anos) > 21:
                self.crescer(0.5 * (21 - self.idade))
            else:
                self.crescer(0.5 * anos)
        self.idade += anos

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros
        
    def __str__(self):
        return f"Pessoa chamada {self.nome} com {self.idade} anos de idade, pesa {self.peso:g}kg e mede {self.altura:g}cm."

# Testes
pessoa1 = Pessoa('José', 15, 60, 170)
print(pessoa1)
pessoa1.envelhecer(2)
print(pessoa1)
pessoa1.envelhecer(20)
print(pessoa1)