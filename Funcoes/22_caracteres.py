# Praticando Python | 022 | Código | Faça como eu fiz: contador de caracteres

# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

'''Função | Ler Palavra com limite mínimo e máximo de caracteres'''
def ler_palavra(msg: str, min_len: int = 1, max_len: int = 46) -> str:

    # laço infinito (repetir até estar correto) | ele encerra no return.
    while True:
        # .strip() remove espaços extras
        p = input(msg).strip()

        # Verifica se a palavra está preenchida com vazio 
        if not p:
            print("Erro: digite uma palavra.")
            continue

        # Verifica se há espaço dentro da palavra, exemplo: "Osasco SP"
        if " " in p:
            print("Erro: digite apenas uma palavra, sem espaços.")
            continue

        # Mínimo de caracteres | A menor palavra do português é o artigo “a”, com apenas 1 caractere.
        if len(p) < min_len:
            print(f"Erro: a palavra deve ter pelo menos {min_len} caracteres.")

        # Máximo de caracteres | “pneumoultramicroscopicossilicovulcanoconiótico” - possui 46 caracteres.
        if len(p) > max_len:
            print(f"Erro: a palavra não pode ter mais que {max_len} caracteres. "
                  f"Você digitou {len(p)}.")
            continue

        # Permitir hífen ou apóstrofo em nomes, exemplo Ana-Julia ou d'Jalma 
        permitido = p.replace("-", "").replace("'", "")
        if not permitido.isalpha():
            print("Erro: use apenas letras, se precisar pode usar o hífen (-) ou apóstrofo (').")
            continue

        # Se tudo estiver correto, encera a função e retornar a palavra.
        return p
        
# Chamar a função
palavra = ler_palavra("Digite a palavra desejada: ", min_len=1, max_len=46)
print(f"A palavra '{palavra}' possui {len(palavra)} caracteres.")