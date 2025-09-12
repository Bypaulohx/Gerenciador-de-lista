import os
from functions.adicionar import adicionar
from functions.mostrar import mostrar
from functions.exibir_item import exibir_item
from functions.ordenar import ordenar
from functions.busca import busca_linear

def menu():
    TAM = 5
    produtos = [None] * TAM
    qtd = [0]
    opcao = -1

    while opcao != 7:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n=== MENU DA LISTA ===")
        print("0 - Resetar a lista")
        print("1 - Adicionar produto")
        print("2 - Mostrar todos os produtos")
        print("3 - Ver tamanho da lista")
        print("4 - Consultar produto por posição")
        print("5 - Ordenar lista por código")
        print("6 - Procurar produto por código")
        print("7 - Encerrar programa")

        try:
            opcao = int(input("\nEscolha uma opcao: "))
        except ValueError:
            opcao = -1

        os.system("cls" if os.name == "nt" else "clear")

        if opcao == 0:
            qtd[0] = 0
            print("\nLista reiniciada!\n")
        elif opcao == 1:
            adicionar(produtos, qtd, TAM)
        elif opcao == 2:
            mostrar(produtos, qtd[0])
        elif opcao == 3:
            print(f"\nA lista contém {qtd[0]} produto(s).\n")
        elif opcao == 4:
            exibir_item(produtos, qtd[0])
        elif opcao == 5:
            ordenar(produtos, qtd[0])
        elif opcao == 6:
            codigo = int(input("\nDigite o código para busca: "))
            pos = busca_linear(produtos, codigo, qtd[0])
            if pos == -1:
                print("\n⚠️ Lista vazia!\n")
            elif pos == -2:
                print("\n⚠️ Código não encontrado!\n")
            else:
                prod = produtos[pos]
                print(f"\n✅ Produto encontrado: Código {prod['codigo']} | Nome: {prod['nome']} (posição {pos+1})\n")
        elif opcao == 7:
            print("\nEncerrando o programa...\n")
        else:
            print("\n⚠️ Opção inválida!\n")

        input("\nPressione ENTER para continuar...")
