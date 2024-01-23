# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro
#     Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#     calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

inputDoUtilizador = [
    float(input("Introduza o numero de litros vendidos: ")),
    input("Introduza o tipo de gasolina(A/G): "),
]

def valorAPagar(abastecimento):
    if (abastecimento[1] == 'A'):
        return (abastecimento[0]*1.9*0.95 if (abastecimento[0] > 20) else abastecimento[0]*1.9*0.97)
    if (abastecimento[1] == 'G'):
        return (abastecimento[0]*2.5*0.94 if (abastecimento[0] > 20) else abastecimento[0]*2.5*0.96)
    return 'Tipo de combustivél não reconhecido'

print(valorAPagar(inputDoUtilizador))
