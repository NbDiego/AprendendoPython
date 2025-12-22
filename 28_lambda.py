# Praticando Python | 028 | Código | Faça como eu fiz: calculadora com lambda

# Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

# Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

# Exemplo:
# Digite o primeiro número: 10   
# Digite o segundo número: 5   
# Escolha a operação (| + | - | * | / |): + 

# Racional
# Criar uma calculadora que:
# 1 - Recebe dois números.
# 2 - Recebe um operador (+, -, *, /).
# 3 - Usa funções lambda para realizar a operação.
# 4 - Exibe o resultado.

# ===================================================================================== #
# ENTRADA | Ler Números                                                                 #
# ===================================================================================== #

# Função para ler um número
def ler_numero(msg: str) -> float:
    while True:
        texto = input(msg).strip()
        try:
            # Tenta converter para float
            return float(texto)
        except ValueError:
            print("Entrada inválida. Digite um número válido (ex.: 10, 5.5, -3).")

# Função para ler o operador (+, -, *, /)
def ler_operador(msg: str) -> str:
    operadores_validos = {'+', '-', '*', '/'}
    while True:
        op = input(msg).strip()
        if op in operadores_validos:
            return op
        else:
            print("Operador inválido. Escolha entre: +, -, * ou /.")

# ===================================================================================== #
# PROCESSAMENTO | Operações com Lambda                                                  #
# ===================================================================================== #

# Dicionário que associa cada operador a uma função lambda correspondente
operacoes = {
                "+": lambda a, b: a + b,     # soma
                "-": lambda a, b: a - b,     # subtração
                "*": lambda a, b: a * b,     # multiplicação
                "/": lambda a, b: a / b if b != 0 else None  # divisão (trata divisão por zero)
            }

# ===================================================================================== #
# SAÍDA | Executar e Mostrar o Resultado                                                #
# ===================================================================================== #

def main():
    print('===== Essa é a calculadora com funções lambda =====')
    n1 = ler_numero('Digite o 1º número: ')
    n2 = ler_numero('Digite o 2º número: ')
    operador = ler_operador('Escolha a operação que deja realizar (| + | - | * | / |): ')

    # Obtém a função lambda correspondente ao operador
    funcao = operacoes[operador]

    # Calcula o resultado (com tratamento para divisão por zero)
    resultado = funcao(n1, n2)

    if resultado is None:
        print('Erro: Você não pode realizar divisão por zero!')
    else:
        # Formata mostrando operação e resultado
        print(f'Resultado: {n1} {operador} {n2} = {resultado}')

# ===================================================================================== #
# MENU PRINCIPAL                                                                        #
# ===================================================================================== #

if __name__ == "__main__":
    main()