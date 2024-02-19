
def indexDoisMaiores(numeros: list):
    return numeros.index(sorted(numeros)[-2:][0]), numeros.index(sorted(numeros)[-2:][1])

print(indexDoisMaiores([3,1,4,2]))

