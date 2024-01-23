# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#     Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
#     Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 

inputDoUtilizador = [
    float(input("Introduza a quantidade de morangos em kg: ")),
    float(input("Introduza a quantidade de maçãs em kg: "))
]

def valorAPagar(abastecimento):
    # desconto 10% se mais k 25$ ou 8kg
    # desconto = False
    if ( ((abastecimento[0] + abastecimento[1]) > 8 ) or ((abastecimento[0]*2.5 + abastecimento[1]*1.8) > 25) ): desconto = True
    if (desconto): print('Desconto de 10%!')
    return ((2.5*abastecimento[0] + 1.8*abastecimento[1])*0.9) if (desconto == True) else (2.5*abastecimento[0] + 1.8*abastecimento[1])

print(f'Tem a pagar {valorAPagar(inputDoUtilizador):g}€')