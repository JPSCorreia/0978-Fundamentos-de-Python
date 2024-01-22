# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes.

#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento. 

inputDoUtilizador = int(input('introduza o seu salário: '))

def ajustarSalario(salario):
    if (salario <= 280):
        return [salario, 20, salario*0.2, salario*1.2]
    if (280 < salario <= 700):
        return [salario, 15, salario*0.15, salario*1.15]
    if (700 < salario <= 1500):
        return [salario, 10, salario*0.1, salario*1.1]    
    else:
        return [salario, 5, salario*0.05, salario*1.05] 

salarioAjustado = ajustarSalario(inputDoUtilizador)


print(f'O salário era de {salarioAjustado[0]:g}€.')
print(f'Recebeu um aumento de {salarioAjustado[1]:g}%.')
print(f'O valor do aumento foi de {salarioAjustado[2]:g}€.')
print(f'O novo salário após o aumento é {salarioAjustado[3]:g}€.')
