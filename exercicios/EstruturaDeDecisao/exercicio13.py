# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 

inputDoUtilizador = int(input('introduza o dia da semana em numero: '))

def escolherDiaDaSemana(dia):
    match dia:
        case 1:
            return "Segunda"
        case 2:
            return "Terça"
        case 3:
            return "Quarta"
        case 4:
            return "Quinta"
        case 5:
            return "Sexta"
        case 6:
            return "Sabado"
        case 7:
            return "Domingo"
        case _:
            return "Valor Inválido!"

print(escolherDiaDaSemana(inputDoUtilizador))