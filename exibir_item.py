def exibir_item(lista, qtd):
    if qtd == 0:
        print("\n⚠️ Lista está vazia!\n")
        return
    pos = int(input("\nInforme a posição desejada: ")) - 1
    if pos < 0 or pos >= qtd:
        print("\n⚠️ Posição inválida ou não preenchida!\n")
    else:
        prod = lista[pos]
        print(f"\nNa posição {pos+1}: Código {prod['codigo']} | Nome: {prod['nome']}\n")
