# Praticando Python | 014 | Código | Calculando a soma de números

# Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
# Crie um programa para implementar a soma.

'''Lista para somar valores'''
valores = [10, 20, 30, 40, 50]

'''Inicializar a variável'''
saldo = 0

'''Laço de Repetição | Executar enquanto houver números na lista'''
for valor in valores:
    saldo += valor
    print(f"O Saldo da sua receita é de R$: {saldo}")