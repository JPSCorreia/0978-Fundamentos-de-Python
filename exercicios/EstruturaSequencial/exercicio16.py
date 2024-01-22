# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

areaAPintar = int(input('insira o tamanho da área a pintar em m²: '))
litrosTintaNecessarios = areaAPintar / 3
latasNecessarias = math.ceil(litrosTintaNecessarios / 18)
custoPorLata = 80
if latasNecessarias <= 1: print(f'Vai precisar apenas uma lata e o custo vai ser {custoPorLata} €.')
else: print(f'Vai precisar {latasNecessarias} latas e o custo vai ser de {custoPorLata*latasNecessarias} €.')