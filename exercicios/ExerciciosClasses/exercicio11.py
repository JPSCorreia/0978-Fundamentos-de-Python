# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

#     Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
#     O consumo é especificado no construtor e o nível de combustível inicial é 0.
#     Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
#     Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
#     Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

#     meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
#     meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
#     meuFusca.andar(100);            # anda 100 quilômetros.
#     meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.


class Carro:

    def __init__(self, consumoCombustivel):
        self.consumoCombustivel = consumoCombustivel / 100 # litro / km 
        self.tanqueCombustivel = 0
    
    def andar(self, distancia):
        self.tanqueCombustivel -= (distancia * self.consumoCombustivel)
    
    def adicionarGasolina(self, quantidade):
        self.tanqueCombustivel += quantidade 
    
    def obterGasolina(self):
        print(self.tanqueCombustivel) 
    
    def __str__(self):
        return f'Carro com consumo {self.consumoCombustivel*100}L / 100km e {self.tanqueCombustivel}L no tanque.'

# Testes
porsche = Carro(9.5)
print(porsche)
porsche.adicionarGasolina(50)
print(porsche)
porsche.andar(250)
print(porsche)
porsche.obterGasolina()