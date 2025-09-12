def mostrar(lista, qtd):
    if qtd == 0:
        print("\n⚠️ Lista ainda está vazia!\n")
    else:
        print("\nProdutos cadastrados:")
        for i in range(qtd):
            print(f"{i+1} → Código: {lista[i]['codigo']} | Nome: {lista[i]['nome']}")
