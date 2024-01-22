# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#     Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#     entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

inputDoUtilizador = [
    input("Telefonou para a vítima?(s/n) "),
    input("Esteve no local do crime?(s/n) "),
    input("Mora perto da vítima?(s/n) "),
    input("Devia para a vítima?(s/n) "),
    input("Já trabalhou com a vitima?(s/n) "),
]


def investigacao(respostas):
    nivelDeSuspeita = respostas.count("s")
    return (
        "Assassino."
        if (nivelDeSuspeita == 5)
        else (
            "Cumplice."
            if ((nivelDeSuspeita == 3) or (nivelDeSuspeita == 4))
            else (
                "Suspeito." if (nivelDeSuspeita == 2) else "Inocente.")
        )
    )


print(investigacao(inputDoUtilizador))
