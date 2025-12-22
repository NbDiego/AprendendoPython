# Praticando Python | 004 | Código | Calculando o IMC

# Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

'''Obter peso e altura'''
peso = float(input('Digite seu peso (kg) use ponto no lugar da virgula, ex. 125.8: '))
altura = float(input('Digite sua altura (m) use ponto no lugar da virgula, ex. 1.80 : '))

'''Calculando o IMC'''
imc = peso / (altura ** 2)

# ** é o operador de potência.
# altura ** 2 = altura ao quadrado.
# peso / (altura ** 2) = peso dividido por altura (ao quadrado)

'''Resultado do IMC'''
print(f"Seu IMC é: {imc:.2f}")
# {imc:.2f} formata o número com 2 casas decimais
# :.2f → “formato float com 2 casas”.

'''Classificar o peso'''
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")