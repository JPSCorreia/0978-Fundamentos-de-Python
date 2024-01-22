# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 

inputDoUtilizador = input('introduza o seu turno(M, V ou N): ')

def escolherMensagemDeTurno(turno):
    match turno:
        case "M":
            return "Bom Dia!"
        case "V":
            return "Boa Tarde!"
        case "N":
            return "Boa Noite!"
        case _:
            return "Valor Inválido!"

print(escolherMensagemDeTurno(inputDoUtilizador))