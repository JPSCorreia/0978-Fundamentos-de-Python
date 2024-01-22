# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

import datetime

inputDoUtilizador = input("introduza uma data com o formato dd/mm/aaaa: ")

def validarData(data):
    # Formata a data que o utilizador introduziu e utiliza a função datetime para verificar se dia, mes e ano sao valores válidos.
    try:
        dia, mes, ano = map(int, data.split("/"))
        datetime.datetime(ano, mes, dia)
        return True
    # Se a função datetime der erro ele retorna False.
    except ValueError:
        return False

print('Data válida' if validarData(inputDoUtilizador) else 'Data inválida')
