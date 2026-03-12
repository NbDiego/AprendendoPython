# [Projeto] Identificando palavras mais longas em um texto

# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras.
# Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

# ================================================================================= #
# Funções do Programa                                                               #
# ================================================================================= #

'''Função | Ler o texto antes de executar o programa'''
def solicitar_texto() -> str:
    while True:
        # Texto do usuário
        txt = input('Digite um texto: \n')

        # Garantir que o usuário não deixe o conteudo vazio ou apenas com espaços.
        if txt.strip() == "":
            print('Erro: O texto não pode ser vazio, digite novamente.\n')
            continue
        
        return txt

'''Função | Encontrar palavras com mais de 10 letras'''
def palavras_acima_de_n(texto: str, n: int = 10) -> list[str]:

    # Separar por espaços em branco
    palavras = texto.split()  

    # Retornar uma lista com as palavras do texto que possuem mais de 10 letras.
    longas = [p for p in palavras if len(p) > n]
    return longas

# ================================================================================= #
# Menu do Programa                                                                  #
# ================================================================================= #
if __name__ == "__main__":

    # Entrada
    txt_usuario = solicitar_texto()

    # Processamento
    palavras_longas = palavras_acima_de_n(txt_usuario, n=10)

    # Saída

    print('\n' + '=' * 55)
    print('Contador de Palavras'.center(55))
    print('=' * 55)
    print('Palavras com mais de 10 letras:')
    print('=' * 55)

    if palavras_longas:
        for idx, p in enumerate(palavras_longas, start=1):
            print(f'{idx:>2}. {p}')
        print('\nResumo:')
        print(f'• {"Leitura do texto":<35} ✅')
        print(f'• {"Procura por palavras > 10 letras":<35} ✅')
        print(f'• {("Total encontradas: " + str(len(palavras_longas))):<35} ✅')
        print('=' * 55)
        print('Programa encerrado com sucesso.')
        print('=' * 55)
        print('')
    else:
        print('Nenhuma palavra longa foi encontrada no texto.')
        print('\nResumo:')
        print(f'• {"Leitura do texto":<35} ✅')
        print(f'• {"Procura por palavras > 10 letras":<35} ✅')
        print(f'• {"Nenhuma encontrada":<35} ⚠️')
        print('=' * 55)
        print('Programa encerrado com sucesso.')
        print('=' * 55)  
        print('') 

# Autor......: Diego Noberto Diniz
# GitHub.....: https://github.com/NbDiego
# Projeto....: Calculadora de Gorjeta
# Criado em..: 26/12/2025 