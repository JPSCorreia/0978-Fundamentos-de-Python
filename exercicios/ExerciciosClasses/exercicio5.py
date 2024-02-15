# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
# com valor default zero e os demais atributos são obrigatórios. 

class ContaCorrente:
    
    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nome = novoNome
    
    def depositar(self, valor):
        self.saldo += valor
    
    def levantar(self, valor):
        self.saldo -= valor
    
    def __str__(self):
        return f"Conta numero {self.numero}, nome {self.nome} com {self.saldo}€."

# Testes
conta1 = ContaCorrente(1, 'José', 500)
conta1.depositar(50)
print(conta1)