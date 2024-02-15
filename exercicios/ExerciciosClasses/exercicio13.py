# Classe Funcionário: Implemente a classe Funcionário. 
# Um empregado tem um nome (um string) e um salário(um double). 
# Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
# Escreva um pequeno programa que teste sua classe. 
from numbers import Number

class Funcionario:
    
    def __init__(self, nome: str, salario: Number):
        self.nome = nome
        self.salario = salario

    def devolverNome(self) -> str:
        return self.nome

    def devolverSalario(self) -> Number:
        return self.salario

funcionario1 = Funcionario('José', 500)

print(funcionario1.devolverSalario())
print(funcionario1.devolverNome())