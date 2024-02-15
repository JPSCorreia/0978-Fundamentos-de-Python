
# Classe Tamagotchi Melhorada: Aperfeiçoe o programa do Tamagotchi, permitindo que o utilizador 
# especifique a quantidade de comida fornecida ao Tamagotchi e o tempo dedicado a brincar com ele. 
# Faça com que esses valores afetem a taxa de diminuição dos níveis de fome e tédio.

class Tamagotchi:


    def __init__(self, nome, fome, saude, idade, comida, tempoBrincar):
        self.nome = nome
        self.fome = max(0, min(100, fome))
        self.saude = saude
        self.idade = idade
        self.tempoBrincar = max(0, min(100, tempoBrincar))
        
    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alterarFome(self, novoFome):
        self.fome = novoFome
        self.fome = max(0, min(100, novoFome))

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
