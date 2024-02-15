# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. 

def menorMaiorSoma(numeros):
    numeros.sort()
    return [numeros[0], numeros[len(numeros)-1], sum(numeros)]

def pedirValoresAoUtilizador():
    valorIsNumber = True
    while (valorIsNumber):
        try: 
            valor = -1
            while(valor < 0 or valor > 1000):
                valor = int(input('Insira um valor entre 0 e 1000: '))
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
