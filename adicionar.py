def adicionar(lista, contador, limite):
    if contador[0] == limite:
        print("\n⚠️ Lista já está cheia!\n")
    else:
        codigo = int(input("\nDigite o código do produto: "))
        nome = input("Digite o nome do produto: ")
        lista[contador[0]] = {"codigo": codigo, "nome": nome}
        contador[0] += 1
