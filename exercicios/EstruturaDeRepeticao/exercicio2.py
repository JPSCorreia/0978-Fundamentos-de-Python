# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 


inputDoUtilizador = ['', '']
while (inputDoUtilizador[0] == inputDoUtilizador[1]):
    inputDoUtilizador = [
        input("Introduza um nome: "),
        input("Introduza uma password: ")
    ]
    if (inputDoUtilizador[0] == inputDoUtilizador[1]): print('Erro: nome e password não podem ser iguais.')
print('Utilizador registado com sucesso!')