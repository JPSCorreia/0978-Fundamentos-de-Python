# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                           Até 5 Kg           Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#     Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 

inputDoUtilizador = [
    input("Introduza o tipo de carne que deseja comprar: (f)ile duplo, (a)lcatra ou (p)icanha "),
    float(input("Introduza a quantidade de carne em kg: ")),
    input("Deseja pagar com cartão(s/n)?  ")
]

def tipoDeCarne(carne):
    match carne:
        case 'f':
            return('File Duplo')
        case 'a':
            return('Alcatra')
        case 'p':
            return('Picanha')
        case _:
            return('Erro')


def precoTotal(carne, quantidade):
    match carne:
        case 'File Duplo':
            return( (quantidade*4.9) if (quantidade <= 5) else (quantidade*(5.8)) )
        case 'Alcatra':
            return( (quantidade*5.9) if (quantidade <= 5) else (quantidade*(6.8)) )
        case 'Picanha':
            return( (quantidade*6.9) if (quantidade <= 5) else (quantidade*(7.8)) )
        case _:
            return('Erro')

def tipoDePagamento(pagouComCartao):
    return 'cartão Tabajara' if (pagouComCartao == 's') else 'dinheiro'

def descontoCartao(pagouComCartao):
    return 'desconto de 5%' if (pagouComCartao == 's') else 'sem desconto'

def valorAPagar(precoTotal, descontoCartao):
    return (precoTotal*0.95) if (descontoCartao == 'desconto de 5%') else precoTotal

def descontoQuantidade(quantidade):
    return 0.9 if (quantidade < 5) else 1


def gerarCupao(abastecimento):
    print('')
    print('---------------------------------------------------------------')
    print(f'{abastecimento[1]:g} kilos de {tipoDeCarne(abastecimento[0])}.')
    print(f'Preço: {precoTotal(tipoDeCarne(abastecimento[0]), abastecimento[1]):g}€')
    print(f'Pagou com {tipoDePagamento(abastecimento[2])}, {descontoCartao(abastecimento[2])}.')
    print(f'Valor a pagar: {valorAPagar(precoTotal(tipoDeCarne(abastecimento[0]), abastecimento[1]), descontoCartao(abastecimento[2])):g}€')
    print('---------------------------------------------------------------')

gerarCupao(inputDoUtilizador)












#     if ( ((abastecimento[0] + abastecimento[1]) > 8 ) or ((abastecimento[0]*2.5 + abastecimento[1]*1.8) > 25) ): desconto = True
#     if (desconto): print('Desconto de 10%!')
#     return ((2.5*abastecimento[0] + 1.8*abastecimento[1])*0.9) if (desconto == True) else (2.5*abastecimento[0] + 1.8*abastecimento[1])

# print(f'Tem a pagar {valorAPagar(inputDoUtilizador):g}€')