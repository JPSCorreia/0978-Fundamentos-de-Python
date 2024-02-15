# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 

escolhaDoUtilizador = 's'
while (escolhaDoUtilizador == 's'):
    populacaoPaisA = int(input("Introduza a população do país A: "))
    populacaoPaisB = int(input("Introduza a população do país B: "))
    taxaCrescimentoA = float(input("Introduza a taxa de crescimento do país A: "))
    taxaCrescimentoB = float(input("Introduza a taxa de crescimento do país B: "))
    numeroDeAnos = 0
    while (populacaoPaisA < populacaoPaisB):
        populacaoPaisA += populacaoPaisA*taxaCrescimentoA
        populacaoPaisB += populacaoPaisB*taxaCrescimentoB
        numeroDeAnos += 1
    print(f'Foram precisos {numeroDeAnos} anos para que a população do País A ultrapassasse a do País B.')    
    escolhaDoUtilizador = input("Quer correr o programa de novo? 's' se sim: ")
print('Programa terminado.')


