# Praticando Python | 002 | Código | Calculando o tempo total de projeto

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

'''Essa função recebe um parâmetro msg (a mensagem que aparecerá no input) e retorna um int.'''
def ler_dias (msg: str) -> int:
    valor = int(input(msg))
    while valor <= 0:
        if valor == 0:
            print("Erro: a quantidade de dias não pode ser igual a zero. Digite novamente.")
        elif valor <0:
            print("Erro: a quantidade de dias não pode ser negativa. Digite novamente.")
        valor = int(input(msg))
    return valor

'''Obter o número de dias por atividade'''
atividade_1 = ler_dias('Informe a quantidade de dias para realizar a 1º Atividade: ')
atividade_2 = ler_dias('Informe a quantidade de dias para realizar a 2º Atividade: ')
atividade_3 = ler_dias('Informe a quantidade de dias para realizar a 3º Atividade: ')

'''Calcular o tempo total do projeto'''
tempo_total = atividade_1 + atividade_2 + atividade_3

'''Apresentar Resultado'''
print(f'O tempo total do projeto é de {tempo_total} dias.')