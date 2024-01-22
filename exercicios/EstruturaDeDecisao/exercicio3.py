# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

inputDoUtilizador = input('introduza se é homem(H) ou mulher(M): ')

def saberGenero(genero):
    (genero == 'H') and print('Homem') or (genero == 'M') and print('Mulher') or (genero != 'H' and  genero != 'M') and print('Sexo Invalido')

saberGenero(inputDoUtilizador)
