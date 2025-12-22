# Praticando Python | 011 | Código | Compreendendo laços

# Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.

# Ajude Ana a decidir entre usar um laço for ou while. Escreva o programa usando o laço que você acredita ser mais adequado para essa tarefa e explique por que escolheu esse laço.

'''Criar a lista de clientes'''
clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

# Racional
# Para cada cliente desta lista, faça um print
# o uso do for nesse caso ajuda, pois eu sei conjunto de itens que quero percorrer, no caso uma lista.
# Quando penso no uso do While, penso mais em uma situação de validação, repetir enquanto uma condição for verdadeira.