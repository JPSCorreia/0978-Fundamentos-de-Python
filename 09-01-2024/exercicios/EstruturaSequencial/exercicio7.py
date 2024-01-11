#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoPorHora = float(input('introduza quanto ganha por hora: '))
numeroDeHoras = float(input('introduza quantas horas trabalha por mês: '))
print(f'Ganha: {int(ganhoPorHora*numeroDeHoras)} €')
