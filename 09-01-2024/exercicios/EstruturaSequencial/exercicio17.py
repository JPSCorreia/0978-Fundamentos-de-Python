# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

#libraries
import math

tamanhoEmMB = int(input('\nInsira o tamanho do arquivo para download em MB: '))
velocidadeInternet = int(input('\nInsira a velocidade da sua internet em Mbps: '))

tempoDeDownloadTotal = math.ceil((tamanhoEmMB/(velocidadeInternet/8)))
tempoDeDownloadMinutos = math.floor(tempoDeDownloadTotal/60)
tempoDeDownloadSegundos = tempoDeDownloadTotal % 60

print(f'\nTempo necessário para download: ' + (f'{tempoDeDownloadMinutos}m e ' if (tempoDeDownloadMinutos > 0) else '') + (f'{tempoDeDownloadSegundos}s' if (tempoDeDownloadSegundos > 0) else ''))  