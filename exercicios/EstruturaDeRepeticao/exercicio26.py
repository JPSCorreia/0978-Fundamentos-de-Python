# Numa eleição existem três candidatos.
# Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

numDeCandidatos = 3
votosCandidato1, votosCandidato2, votosCandidato3, votosInvalidos = 0, 0, 0, 0


def votar():
    voto = int(input("Introduza o numero do candidato em que quer votar (1, 2 ou 3): "))
    match voto:
        case 1:
            votosCandidato1 += 1
        case 2:
            votosCandidato2 += 1
        case 3:
            votosCandidato3 += 1
        case _:
            votosInvalidos += 1


def pedirVotos(numeroDeEleitores):
    for i in range(0, numeroDeEleitores):
        votar()


def mostrarVotacao():
    print(f"O numero de votos no 1º candidato é: {votosCandidato1}")
    print(f"O numero de votos no 2º candidato é: {votosCandidato2}")
    print(f"O numero de votos no 3º candidato é: {votosCandidato3}")
    print(f"O numero de votos invalidos é: {votosInvalidos}")


pedirVotos(int(input("Introduza o numero total de eleitores: ")))
mostrarVotacao()
