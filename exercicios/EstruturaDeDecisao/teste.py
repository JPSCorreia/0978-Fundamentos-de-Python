def maiorOuMenor(n1, n2):
    return n1 if (n1 > n2) else n2


numero3 = maiorOuMenor(maiorOuMenor(1, 2), 10)

def nmaiormenor():
    nr1 = input("Digite nr")
    nr2 = input("digit 2nr")
    if nr1 > nr2:
        print(nr1)
    else :
        print(nr2)
nmaiormenor()