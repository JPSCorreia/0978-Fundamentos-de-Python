# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve 
# pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

quantidadeDePeixe = int(input('introduza a quantidade de peso em kilos: '))
quantidadeEmExcessoDePeixe = quantidadeDePeixe - 50

if (quantidadeEmExcessoDePeixe < 0): quantidadeEmExcessoDePeixe = 0
multa = 4 * quantidadeEmExcessoDePeixe

if (multa > 0): print(f'Tem de pagar uma multa de {multa} €.')
if (multa == 0): print(f'Não tem qualquer multa a pagar')

