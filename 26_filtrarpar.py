# Praticando Python | 026 | Código | Faça como eu fiz: filtrando números pares

# Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

# Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

# Racional
# Número par: um número é par se o resto da divisão por 2 for igual a zero → n % 2 == 0.
# filter(funcao, iterable): percorre os itens e mantém apenas aqueles para os quais a função retorna True.
# Entrada                     : ler números digitados pelo usuário em uma linha (separados por espaço).
# Processamento               : converter para int e usar filter() com uma função que testa se é par.
# Saída (Formulário Principal): exibir apenas os pares.

# ===================================================================================== #
# Entrada | Interação com o usuário                                                     #
# ===================================================================================== #

'''Função | Listar Números'''
def ler_numeros(msg: str) -> list[int]:
    # Laço infinito
    while True:
        # .strip() para remover espaços
        entrada = input(msg).strip()

        # Verificar se entrada está vazio, sem nada
        if not entrada:
            print('Erro: É necessario digitar um número!')
            continue

        # split() Quebrar a string em partes ("1 2 3" → ["1", "2", "3"]).
        partes = entrada.split()

        # Aqui vamos criar uma lista vazia, a ideia é guardar os inteiros convertidos
        numeros = []

        # Aqui algo pode dar errado, por isso estou usando o try (tente executar esse bloco)
        try:
            # Vamos listar número a número
            for p in partes:
                # append(...): Adiciona o inteiro convertido à lista numeros
                numeros.append(int(p))
            return numeros
        
        # Se o int der algum erro, ele vai entrar aqui
        except ValueError:
            print('Erro: Experimente digitar um número inteiro, exe: 1 2 3')

# ===================================================================================== #
# Processamento                                                                         #
# ===================================================================================== #
'''Função | Validar se o número é par'''
def eh_par(n: int) -> bool:
    return n % 2 == 0

'''Função | Filtrar números pares'''
def filtrar_pares(numeros: list[int]) -> list[int]:
    return list(filter(eh_par, numeros))

# ===================================================================================== #
# Formulário Principal                                                                  #
# ===================================================================================== #
if __name__ == "__main__":
    # Entrada
    numeros = ler_numeros("Digite números separados por espaço: ")

    # Processamento
    pares = filtrar_pares(numeros)

    # Saída
    print("\nRelatório – Números pares")
    print(f"Entrada: {numeros}")
    print(f'Esses são os números {pares} pares.')