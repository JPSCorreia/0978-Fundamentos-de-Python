# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, q
# ue depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#             Salário Bruto: (5 * 220)        : R$ 1100,00
#             (-) IR (5%)                     : R$   55,00  
#             (-) INSS ( 10%)                 : R$  110,00
#             FGTS (11%)                      : R$  121,00
#             Total de descontos              : R$  165,00
#             Salário Liquido                 : R$  935,00

inputDoUtilizador = [float(input('introduza quanto ganha á hora: ')), int(input('introduza quantas horas trabalhou no mês: '))]

def calcularFolhaPagamentos(ganhoPorHora, numeroDeHoras):
    salarioBruto = ganhoPorHora * numeroDeHoras
    
    if (salarioBruto <= 900):
        taxaIR = 0
    elif (900 < salarioBruto <= 1500):
        taxaIR = 0.05
    elif (1500 < salarioBruto <= 2500):
        taxaIR = 0.1d
    else:
        taxaIR = 0.2
    
    taxaSindicato = 0.03
    taxaFGTS = 0.11
    totalDescontos = (salarioBruto*taxaIR) + (salarioBruto*taxaSindicato)
    salarioLiquido = salarioBruto - totalDescontos
    
    return {
        "ganhoPorHora": ganhoPorHora, 
        "numeroDeHoras": numeroDeHoras, 
        "salarioBruto": salarioBruto, 
        "taxaIR": taxaIR,
        "taxaSindicato": taxaSindicato,
        "taxaFGTS": taxaFGTS,
        "totalDescontos": totalDescontos,
        "salarioLiquido": salarioLiquido,
    }

def apresentarFolhaPagamentos(folhaDePagamentos):
    print('')
    print(f"Salário Bruto: ({folhaDePagamentos['ganhoPorHora']} * {folhaDePagamentos['numeroDeHoras']})      : R$ {folhaDePagamentos['salarioBruto']}")
    print(f"(-) IR ({(folhaDePagamentos['taxaIR'] * 100):g}%)                     : R$  {(folhaDePagamentos['taxaIR'])*folhaDePagamentos['salarioBruto']}")
    print(f"(-) INSS ({(folhaDePagamentos['taxaSindicato'] * 100):g}%)                   : R$  {(folhaDePagamentos['taxaSindicato'])*folhaDePagamentos['salarioBruto']}")
    print(f"FGTS ({(folhaDePagamentos['taxaFGTS'] * 100):g}%)                      : R$  {(folhaDePagamentos['taxaFGTS'])*folhaDePagamentos['salarioBruto']}")
    print(f"Total de descontos              : R$  {folhaDePagamentos['totalDescontos']}")
    print(f"Salário Liquido                 : R$  {folhaDePagamentos['salarioLiquido']}")

folhaDePagamentosDoUtilizador = calcularFolhaPagamentos(inputDoUtilizador[0], inputDoUtilizador[1])
apresentarFolhaPagamentos(folhaDePagamentosDoUtilizador)

