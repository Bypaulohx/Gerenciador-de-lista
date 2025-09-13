## Sistema de Gerenciamento de Códigos de Produtos

Este projeto em Python permite gerenciar uma lista de códigos de produtos de maneira simples e interativa via menu. Ideal para iniciantes que desejam praticar estruturas de dados, funções e lógica de programação.

## Funcionalidades

Adicionar códigos de produtos à lista.

Mostrar todos os códigos cadastrados.

Consultar tamanho atual da lista.

Consultar código em uma posição específica.

Ordenar a lista em ordem crescente (seleção).

Buscar códigos de forma sequencial (busca linear).

Resetar a lista para iniciar do zero.

## Como usar

Clone o repositório ou faça o download do arquivo main.py.

Execute o programa:
```
python main.py
```
Siga o menu interativo para gerenciar a lista.

## Estrutura da Pasta
```
lista_produtos_functions/
├── __pycache__/
│   └── menu.cpython-311.pyc
├── functions/
│   ├── __init__
│   ├── adicionar.py
│   ├── buscar.py
│   ├── exibir_item.py
│   ├── mostrar.py
│   ├── ordenar.py
│   └── __pycache__/
│       ├── __init__.cpython-311.pyc
│       ├── adicionar.cpython-311.pyc
│       ├── buscar.cpython-311.pyc
│       ├── exibir_item.cpython-311.pyc
│       ├── mostrar.cpython-311.pyc
│       └── ordenar.cpython-311.pyc
├── main.py
└── menu.py
```

> ⚠️ **Observações**:
A lista possui tamanho limitado (por padrão, 5 elementos).
É possível reiniciar a lista a qualquer momento pelo menu.
Entrada de dados inválida ou posições fora do limite são tratadas com mensagens de alerta.

---
