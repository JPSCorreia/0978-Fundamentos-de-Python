# Faça um programa que pergunte o preço de três produtos 
# e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

inputDoUtilizador = [float(input('introduza um preço: ')), float(input('introduza outro preço: ')), float(input('introduza outro preço: '))]

def saberMenor(listaDeNumeros):
    return sorted(listaDeNumeros)[0]

def printProdutosComPrecoMenor(listaDePrecos, preco):
    # Procurar indices do preço mais baixo.
    indicesDePrecoMaisBaixo = []
    for i, valor in enumerate(listaDePrecos):
        if (valor == preco):
            indicesDePrecoMaisBaixo.append(i)
    # Devolver produtos que correspondem aos indices do preço mais baixo.   
    print('Produto/s com preço mais baixo:')  
    for i in indicesDePrecoMaisBaixo:
        print(f'Produto numero {i+1}')

precoMenor = saberMenor(inputDoUtilizador)
printProdutosComPrecoMenor(inputDoUtilizador, precoMenor)

