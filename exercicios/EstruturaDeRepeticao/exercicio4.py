# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

populacaoPaisA = 80000
populacaoPaisB = 200000
taxaCrescimentoA = 0.03
taxaCrescimentoB = 0.015
numeroDeAnos = 0
while (populacaoPaisA < populacaoPaisB):
    populacaoPaisA += populacaoPaisA*taxaCrescimentoA
    populacaoPaisB += populacaoPaisB*taxaCrescimentoB
    numeroDeAnos += 1
print(f'Foram precisos {numeroDeAnos} anos para que a população do País A ultrapassasse a do País B.')    