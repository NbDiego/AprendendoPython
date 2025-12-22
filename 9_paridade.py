# Praticando Python | 009 | Código | Verificando a paridade de um número

# Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

'''Obter o número'''
try:
    numero = int(input('Digite um número inteiro: '))
except ValueError:
    print('Entrada inválida. Digite apenas números inteiros (ex.: -13, -3, 0, 3, 13).')
else:
    '''Premissa | Resto da divisão de um número por 2'''
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')

# Racional utilizado
# o try é usado como: Tente executar esse bloco de código, pois algo pode dar errado...
# o except ValueError estou usando para tratar as situações onde o valor não é valido, exemplo: "abc"
# o else do try, só vai executar o código se não houver erro.
# Racional do calculo
# Se o resto da divisão for igual a zero, é um número par
# Se o resto da divisão não for igual a zero, é número impar.