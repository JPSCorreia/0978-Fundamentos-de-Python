# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato
# Faça um programa que nos dê:
#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.

#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$
#     Obs.: Salário Bruto - Descontos = Salário Líquido. 

ganhoPorHora = float(input('introduza quanto ganha por hora: '))
numeroDeHoras = float(input('introduza quantas horas trabalha por mês: '))
salarioBruto = round(ganhoPorHora*numeroDeHoras, 2)
descontoRenda = salarioBruto*0.11
descontoINSS = salarioBruto*0.08
descontoSindicato = salarioBruto*0.05
salarioLiquido = salarioBruto - descontoRenda - descontoINSS - descontoSindicato

print(f'O seu salario bruto é: {salarioBruto:g} €.')
print(f'descontou para a renda: {descontoRenda:g} €.')
print(f'descontou para o INSS: {descontoINSS:g} €.')
print(f'descontou para o Sindicato: {descontoSindicato:g} €.')
print(f'O seu salario liquido é: {salarioLiquido:g} €.')

