# Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:

#     A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#     A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#     A mensagem "Aprovado com Distinção", se a média for igual a 10. 

inputDoUtilizador= [round(float(input('Introduza uma nota: '))), round(float(input('Introduza outra nota: '))), round(float(input('Introduza uma terceira nota: ')))]

def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota
    
    return ((soma) / len(notas))

def aprovadoOuReprovado(media):
    if (media == 10): return 'Aprovado com Distinção'
    if (media >= 7): return 'Aprovado'
    return 'Reprovado'

print(aprovadoOuReprovado(calcularMedia(inputDoUtilizador)))