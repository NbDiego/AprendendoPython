# Praticando Python | 018 | Código | Contagem Regressiva

# Aline está implementando uma funcionalidade que exibe mensagens personalizadas para os clientes durante uma promoção especial da sua nova loja de livros. O sistema deve exibir uma mensagem de contagem regressiva personalizada para cada número de 10 até 1, e ao final exibir a mensagem: "Aproveite a promoção agora!".
# Crie um programa que utilize um laço for para exibir as seguintes mensagens:
# Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
# Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
# Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".

'''Inicializar a variável de segundos'''
segundos = 10

'''Laço de repetição'''
while segundos >= 1:
    if segundos % 2 == 0:
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {segundos} segundos restantes.")
    segundos -= 1

print("Aproveite a promoção agora!")

# Racional
# Começamos com 10 e vamos até o 1.
# O Zero não vai entrar, pois ele é o Final de tudo.
# -1 uso para reduzir os segundos.