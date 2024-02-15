# Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores. 

def menorMaiorSoma(numeros):
    numeros.sort()
    return [numeros[0], numeros[len(numeros)-1], sum(numeros)]

def pedirValoresAoUtilizador():
    valorIsNumber = True
    while (valorIsNumber):
        try: 
            valor = int(input('Insira um valor: '))
            try: 
                valores.append(valor) 
            except Exception: 
                valores = [valor]
        except Exception: 
            valorIsNumber = False
    return valores

def imprimirResultadoMaiorMenorSoma(resultado):
    print(f'O menor valor é {resultado[0]}, o maior valor é {resultado[1]} e a soma dos valores é {resultado[2]}.')

imprimirResultadoMaiorMenorSoma(menorMaiorSoma(pedirValoresAoUtilizador()))

