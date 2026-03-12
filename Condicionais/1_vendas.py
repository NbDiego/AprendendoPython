# Praticando Python | 001 | Código | Monitorando vendas no comércio

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

'''Receber a quantidade vendida para cada produto'''
macas = int(input('Digite a quantidade de maçãs vendidas: '))
bananas = int(input('Digite a quantidade de bananas vendidas: '))

'''Calcular Diferença'''
if macas > bananas:
    dif_produto = macas - bananas
elif macas < bananas:
    dif_produto = bananas - macas

'''Apresentar Resultado'''
if macas > bananas:
    print(f'Vendemos {dif_produto} maçãs a mais que bananas!')
elif macas < bananas:
    print(f'Vendemos {dif_produto} bananas a mais que maçãs!')
else:
    print('Vendemos a mesma quantidade de maçãs e bananas!')