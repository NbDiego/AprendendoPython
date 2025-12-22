# Praticando Python | 005 | Código | Controlando o orçamento mensal

# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

'''Valor do Limite'''
limite = 3000.0

'''Obter valor da despesa'''
despesa = float(input("Digite o valor da Despesa (R$) use ponto ao invés de virgula, ex 5000.0: "))

'''Calcular Saldo'''
if limite > despesa:
    saldo = limite - despesa
    print(f'Seu saldo é de R$ {saldo}, estamos dentro do orçamento mensal!')
elif limite < despesa:
    saldo = limite - despesa
    print(f'Atenção! você estourou o limete do oraçamento mensal em R$ {saldo}, precisa avaliar a situação!')
elif limite == despesa:
    saldo = limite - despesa
    print(f'Cuidado! esse mês seu limite está zerado, esse é o seu saldo R$ {saldo}')