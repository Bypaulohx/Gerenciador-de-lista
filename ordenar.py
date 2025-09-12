def ordenar(lista, qtd):
    if qtd == 0:
        print("\n⚠️ Lista está vazia!\n")
    else:
        for i in range(qtd - 1):
            menor = i
            for j in range(i + 1, qtd):
                if lista[j]["codigo"] < lista[menor]["codigo"]:
                    menor = j
            lista[i], lista[menor] = lista[menor], lista[i]
        print("\nLista organizada com sucesso!\n")
