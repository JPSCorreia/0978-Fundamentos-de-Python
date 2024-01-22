# Faça um Programa que leia 2 números e em seguida pergunte ao
# usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.

inputDoUtilizador = [
    float(input("digite um numero: ")),
    float(input("digite outro numero: ")),
    input("que operação deseja realizar(+, -, *, /)? "),
]

def fazerOperacao(lista):
    match lista[2]:
        case "+":
            return lista[0] + lista[1]
        case "-":
            return lista[0] - lista[1]
        case "*":
            return lista[0] * lista[1]
        case "/":
            return lista[0] / lista[1]
        case _:
            return "Valor Inválido!"

def tipodeNumero(numero):
    print(f"o resultado da conta é {numero:g}.")
    return (
        "numero é zero"
        if (numero == 0)
        else (
            ("O numero é decimal" if (numero % 1) else "O numero é inteiro")
            + ((", impar" if (numero % 2) else ", par") if (not numero % 1) else "")
            + (" e positivo." if (numero > 0) else " e negativo.")
        )
    )

print(tipodeNumero(fazerOperacao(inputDoUtilizador)))
