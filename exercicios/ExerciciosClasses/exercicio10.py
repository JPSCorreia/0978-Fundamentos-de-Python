# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

#     Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#         tipoCombustivel.
#         valorLitro
#         quantidadeCombustivel 
#     Possua no mínimo esses métodos:
#         abastecerPorValor( ) – método onde é informado o valor a ser abastecido e 
#         mostra a quantidade de litros que foi colocada no veículo
#         abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#         alterarValor( ) – altera o valor do litro do combustível.
#         alterarCombustivel( ) – altera o tipo do combustível.
#         alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba. 
#     OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba. 

class bombaCombustível:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel


    def alterarQuantidadeCombustivel(self, quantidadeAbastecida):
        self.quantidadeCombustivel -= quantidadeAbastecida # altera a quantidade de combustivel restante na bomba.

    def abastecerPorValor(self, valorAAbastecer):
        print(f'A abastecer {valorAAbastecer}€: {round(valorAAbastecer / self.valorLitro, 2)}L.')
        self.alterarQuantidadeCombustivel(round(valorAAbastecer / self.valorLitro, 2))
        return valorAAbastecer / self.valorLitro # devolve litros abastecidos.

    def abastecerPorLitro(self, quantidadeLitros):
        self.alterarQuantidadeCombustivel(quantidadeLitros)
        return quantidadeLitros * self.valorLitro # devolve quanto tem de pagar.

    def alterarValor(self, novoValorDoLitro):
        self.valorLitro = novoValorDoLitro # altera o valor do litro.

    def alterarCombustivel(self, novoTipoDeCombustivel):
        self.tipoCombustivel = novoTipoDeCombustivel # altera o tipo de combustivel.

    def __str__(self):
        return f'Bomba com tipo de combustivel {self.tipoCombustivel} com o custo {self.valorLitro}€ por litro e {self.quantidadeCombustivel}L de combustivel.'

# Testes
galp = bombaCombustível('Sem chumbo', 1.8, 5000)
galp.abastecerPorValor(50)
print(galp)
galp.abastecerPorLitro(200)
print(galp)