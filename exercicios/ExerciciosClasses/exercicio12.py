# Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante 
# a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. 
# Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
# Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. 
# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 
# e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes 
# e imprime o saldo resultante. 

class ContaInvestimento:
    
    def __init__(self, numero, nome, saldo, taxaJuros):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicioneJuros(self):
        self.saldo += self.saldo * (self.taxaJuros / 100)


novaConta = ContaInvestimento(1, 'José', 1000, 10)
novaConta.adicioneJuros()
novaConta.adicioneJuros()
novaConta.adicioneJuros()
novaConta.adicioneJuros()
novaConta.adicioneJuros()
print(novaConta.saldo)