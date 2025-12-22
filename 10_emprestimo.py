# Praticando Python | 010 | Código | Aprovando empréstimo

# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada.
# O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

'''Obter o valor da renda do cliente'''
renda = float(input('Digite o valor da sua renda. Exemplo 13000.00 | R$: '))

'''Obter o valor da parcela'''
parcela = float(input('Digite o valor da parcela que você consegue pagar. Exemplo 300.00 | R$: '))

'''Calcular a Diferença da Renda'''
if renda < 2000:
    dif_renda = 2000 - renda + 1
elif renda > 2000:
    dif_renda = renda - 2000

'''Regra de aprovação | Renda Superior a 2 mil e que não passe de 30% do comprometimento da reda'''
if renda <= 2000:
    print(f'Sua renda R$ {renda} não é suficiente para aprovação do emprestimo, você precisa ter mais R$ {dif_renda} para conseguir a aprovação!')
elif renda > 2000 and parcela >= 0.3 * renda:
    print(f'Sua renda R$ {renda} é suficiente para aprovação, porém o valor da sua parcela R$ {parcela} compromete 30% da renda.')
elif renda > 2000 and parcela <= 0.3 * renda:
    print("Empréstimo aprovado, sua renda e sua parcela está dentro do esperado!")