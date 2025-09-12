def busca_linear(lista, procurado, qtd):
    if qtd == 0:
        return -1
    for i in range(qtd):
        if lista[i]["codigo"] == procurado:
            return i
    return -2
