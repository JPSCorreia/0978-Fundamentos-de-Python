# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade 
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
# Obs: Existe mais uma informação que devemos levar em consideração, 
# o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, 
# então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento. 

class Tamagotchi:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alterarFome(self, novoFome):
        self.fome = novoFome

    def alterarSaude(self, novoSaude):
        self.saude = novoSaude

    def alterarIdade(self, novoIdade):
        self.idade = novoIdade
        
    def devolverNome(self):
        return self.nome 

    def devolverFome(self):
        return self.fome 

    def devolverSaude(self):
        return self.saude

    def devolverIdade(self):
        return self.idade
    
    def humor(self):
        return self.fome + self.saude 
