# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.


def quantidadeDeCDsEValor():
    quantidadeDeCDs = int(input("Introduza a quantidade de CDs: "))
    valorTotalDosCDs = 0
    for i in range(quantidadeDeCDs):
        valorTotalDosCDs += int(input("Introduza o valor de um CD em euros: "))
    return quantidadeDeCDs, valorTotalDosCDs


def valorMedio(valorEQuantidadeDeCDs):
    quantidadeDeCDs, valorTotalDosCDs = valorEQuantidadeDeCDs
    return valorTotalDosCDs / quantidadeDeCDs


print(f"O valor médio de cada CD é {valorMedio(quantidadeDeCDsEValor()):.4g}€.")
