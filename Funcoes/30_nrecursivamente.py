# Praticando Python | 030 | Código | Faça como eu fiz: somando números recursivamente

# Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.
# Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.
# Entrada: Digite um número: 5
# Saida: A soma de 1 a 5 é: 15

# ===================================================================================== #
# ENTRADA | Funções auxiliares para leitura                                             #
# ===================================================================================== #

'''Função | Ler um número inteiro'''
def ler_int(msg: str) -> int:
    while True:
        entrada = input(msg).strip()
        try:
            valor = int(entrada)
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro (ex.: 5).")

# ===================================================================================== #
# PROCESSAMENTO | Funções de cálculo                                                    #
# ===================================================================================== #

'''Função | Somar recursivamente os inteiros de 1 até n.'''
def soma_ate_n_recursivo(n: int) -> int:
    # Parada da recursão
    if n == 0:
        return 0

    # Passo recursivo (reduz o problema): soma atual + soma do menor subproblema
    return n + soma_ate_n_recursivo(n - 1)
#    Regras:
#    - Se n < 0  -> Não tem sentido somar até negativos.
#    - Se n == 0 -> Soma 0 ponto de parada da recursão.
#    - Passo recursivo: n + soma_ate_n_recursivo(n - 1)

# Soma de 1 até n usando laço (for).
def soma_ate_n_iterativo(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

'''Função | Matemática -> n * (n + 1) / 2'''
def soma_ate_n_formula(n: int) -> int:
    return n * (n + 1) // 2  # // para garantir inteiro

# ===================================================================================== #
# SAÍDA | Executar e Mostrar o Resultado                                                #
# ===================================================================================== #

if __name__ == "__main__":
    print("=== Somando números de 1 até n (Recursão) ===\n")

    # ENTRADA
    n = ler_int("Digite um número: ")

    # Validação de negócio
    while n < 0:
        print("Erro: o número deve ser zero ou positivo (n >= 0).")
        n = ler_int("Digite um número: ")

    # PROCESSAMENTO
    resultado = soma_ate_n_recursivo(n)

    # SAÍDA
    print(f"\nA soma de 1 a {n} é: {resultado}")