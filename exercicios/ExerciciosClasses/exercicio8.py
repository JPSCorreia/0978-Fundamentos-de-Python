# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
# e pelo menos os métodos comer(), verBucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos, 
# alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago 
# a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal? 

class Macaco:
    
    def __init__(self, nome, estomago = None):
        self.nome = nome
        # Como está a ser referenciado a mesma lista (estomago = []) quando é
        # criada uma nova instancia da classe então ficam todas a apontar para essa referencia.
        # Para não ter esse problema inicializar estomago como None e:
        self.estomago = estomago if estomago is not None else [] 
    
    def comer(self, alimento):
        self.estomago.append(alimento)
        print(f'{self.nome} comeu {alimento}')
    
    def verEstomago(self):
        print(f'Estomago do {self.nome}: {self.estomago}')
    
    def digerir(self):
        self.estomago = []
        print(f'{self.nome} fez a digestão!')
    
    def __str__(self):
        return f"Macaco {self.nome} com {self.estomago} no estomago."

macaco1 = Macaco('Peanut')
macaco2 = Macaco('Oliver')
macaco1.verEstomago()
macaco2.verEstomago()
macaco1.comer('Banana')
macaco1.verEstomago()
macaco2.verEstomago()
macaco1.comer('Amendoim')
macaco1.comer('Laranja')
macaco1.verEstomago()
macaco2.verEstomago()
macaco1.digerir()
macaco1.verEstomago()
macaco2.verEstomago()
macaco1.comer(macaco2)
macaco1.verEstomago()
macaco2.verEstomago()
print(macaco1.estomago[0])

