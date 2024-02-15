# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (percentualDeAumento) 
# que aumente o salário do funcionário em uma certa percentagem.
#     Exemplo de uso:
#       harry=funcionário("Harry",25000)
#       harry.aumentarSalario(10)
from numbers import Number

class Funcionario:
    
    def __init__(self, nome: str, salario: Number):
        self.nome = nome
        self.salario = salario

    def devolverNome(self) -> str:
        return self.nome

    def devolverSalario(self) -> Number:
        return self.salario
    
    def aumentarSalario(self, valor) -> None:
        self.salario += self.salario*0.1

harry = Funcionario('Harry', 25000)
harry.aumentarSalario(10)

print(harry.devolverSalario())
print(harry.devolverNome())
