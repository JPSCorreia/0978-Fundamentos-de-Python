# Faça um Programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#     Informe ao usuário as quantidades de tinta a serem compradas e 
# os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício 
#     de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores 
#     para cima, isto é, considere latas cheias. 

#libraries
import math

areaAPintar = int(input('insira o tamanho da área a pintar em m²: '))
litrosTintaNecessarios = areaAPintar / 6    
custoPorLata = 80
quantidadeLata = 18
custoPorGaloes = 25
quantidadeGalao = 3.6

print (f'\nVai precisar {math.ceil(litrosTintaNecessarios)} litros de tinta.')

# # Comprar apenas latas de 18 litros.
print('\nCaso 1 (Apenas latas): ')
latasNecessarias = math.ceil(litrosTintaNecessarios / quantidadeLata)
print(f'Vai precisar {latasNecessarias} lata(s) e o custo vai ser de {custoPorLata*latasNecessarias} €.')

# # Comprar apenas galões de 3,6 litros.
print('\nCaso 2 (Apenas galões):')
galoesNecessarios = math.ceil(litrosTintaNecessarios / quantidadeGalao)
print(f'Vai precisar {galoesNecessarios} galão(ões) e o custo vai ser de {custoPorGaloes*galoesNecessarios} €.')

# Misturar latas e galões.
print('\nCaso 3 (Misturar latas e galões):')
numeroDeLatasPrecisas = math.floor(litrosTintaNecessarios / quantidadeLata)
numeroDeGaloesPrecisos = math.ceil(litrosTintaNecessarios % quantidadeLata / quantidadeGalao)
if (numeroDeGaloesPrecisos == 5):
    numeroDeGaloesPrecisos = 0
    numeroDeLatasPrecisas = numeroDeLatasPrecisas + 1


#se for 14.4 litros ou menos usar galões:
if ((litrosTintaNecessarios < (quantidadeLata - quantidadeGalao))): print(f'numero de galoes precisos: {numeroDeGaloesPrecisos}')

# se for entre 14.4 e 18 litros usar uma lata:
if (((litrosTintaNecessarios / quantidadeLata) < 1)): print(f'Vai precisar uma lata e o custo vai ser de {custoPorLata} €.')

# se for mais do que 18 litros usar uma mistura de latas e galões:
if ((litrosTintaNecessarios) > (quantidadeLata)): print(f'Vai precisar {numeroDeLatasPrecisas} lata(s) e {numeroDeGaloesPrecisos} galão(ões) e o preço vai ser {(numeroDeLatasPrecisas*custoPorLata)+(numeroDeGaloesPrecisos*custoPorGaloes)} €.')

