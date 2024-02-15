# Faça um programa que peça para n pessoas a sua idade, 
# ao final o programa devera verificar se a média de idade 
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, 
# dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 

def mediaDeIdades(idades):
    media = sum(idades)/len(idades)
    if (media > 0 and media < 26):
        return 'jovem'
    if (media >= 26 and media < 60):
        return 'adulta'
    if (media >= 60):
        return 'idosa'

idadesDaTurma = []
idade = 0

while (isinstance(idade, int)):
    try: 
        idade = int(input('Introduza uma idade: '))
    except Exception: 
        break
    if (idade > 0): 
        idadesDaTurma.append(int(idade))

print(f'A turma é {mediaDeIdades(idadesDaTurma)}.')