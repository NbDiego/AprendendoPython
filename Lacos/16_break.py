# Praticando Python | 016 | Código | Entendendo o uso do break

# José está desenvolvendo uma funcionalidade no sistema do Buscante para interromper a busca assim que um livro específico é encontrado. A lista de livros já cadastrados no sistema é a seguinte:

# Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.

'''Lista de Livros'''
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

'''Inicializar o contador'''
contador = 0

'''Laço de repetição | executar até encontrar o livro desejado'''
for livro in livros:
    contador += 1
    if livro == "O Hobbit":
        print(f"O Livro {livro} foi encontrado, está na posição {contador} da lista.")
        break
# Racional
# Como o for me permiti percorrer todos os itens da lista, aproveitei essa funcionalidade e criei um contador.
# A ideia do contador é saber em qual linha\posição eu encontrei o dado.
# caso queira, altere o nome do livro e você vai ver que a posição dele muda.