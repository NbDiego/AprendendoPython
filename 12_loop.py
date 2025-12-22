# Praticando Python | 012 | Código | O que é um loop infinito?

# André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.

# Qual é o problema do código de André e como resolver?

'''Iniciar o contador'''
contador = 0

'''Enquanto o contador for menor que 10, faça...'''
while contador < 10:
    print("Processando dados...")
    contador += 1  

# No caso do André o contador estava sempre em Zerado, para corrigir, fiz contador += 1.
# ou seja, ao termino da impressão Processando dados... ele atualiza o contador, contador = contador + 1  
# Início: contador = 0
# contador 0 < 10, então exibir Processando dados... depois o contador soma 1
# contador 1 < 10, então exibir Processando dados... depois o contador soma 1
# ...
# contador 9 < 10, então exibir Processando dados... depois o contador soma 1
# Quando contador 10 < 10 ele vai parar, pois isso não é verdadeiro.