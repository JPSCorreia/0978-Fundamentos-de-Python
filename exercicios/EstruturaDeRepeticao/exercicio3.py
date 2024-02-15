# Faça um programa que leia e valide as seguintes informações:

#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd'; 

nome = ''
idade = -1
salario = -1
sexo = ''
estadoCivil = ''
while (len(nome) < 3): nome = input('Introduza um nome válido: ')
while ((idade < 0) or (idade > 150)): idade = int(input('Introduza uma idade válida: '))
while (salario <= 0): salario = int(input('Introduza um salário: '))
while ((sexo != 'm') and (sexo != 'f')): sexo = input('Introduza o sexo: ')
while ((estadoCivil != 's') and (estadoCivil != 'c') and (estadoCivil != 'v') and (estadoCivil != 'd')): estadoCivil = input('Introduza o estado civil: ')
print('Dados validados.')