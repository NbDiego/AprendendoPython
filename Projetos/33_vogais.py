# Projeto | Contagem de vogais em um texto

# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) em contém.

# ================================================================================= #
# Biblioteca Python                                                                 #
# ================================================================================= #

# Fornece ferramentas para trabalhar com o padrão de caracteres de praticamente todos os idiomas.
import unicodedata

# Ferramenta para gerar contagem de caracteres ou itens de forma simples e rápida.
from collections import Counter

# ================================================================================= #
# Funções do Programa                                                               #
# ================================================================================= #

'''Função | Remover acentuação do texto usando normalização Unicode.'''
def remover_acentos(texto: str) -> str:
    # Separar letras e seus acentos em caracteres distintos
    nf = unicodedata.normalize('NFD', texto)

    # Analisar cada caractere (ch) do texto decomposto (nf).
    sem_acentos = ''.join(ch for ch in nf if unicodedata.category(ch) != 'Mn')

    # Devolver a string sem acentos
    return unicodedata.normalize('NFC', sem_acentos)

'''Função | Contar Vogal'''
def contagem_por_vogal(texto: str) -> dict:

    # Usa a função de remover o acento e depois converte o texto para minúsculas
    texto_sem_acentos = remover_acentos(texto).lower()

    # Aqui estou criando um conjunto com as vogais: {'a', 'e', 'i', 'o', 'u'}.
    vogais = set("aeiou")

    # Criar um contador | Caractere (ch) por Caractere (ch)
    cont = Counter(ch for ch in texto_sem_acentos if ch in vogais)
    
    # Retoanar um dicionário
    return {v: cont.get(v, 0) for v in "aeiou"}
    # cont.get(v, 0):
    # -> Se v existe no Counter, retorna sua contagem.
    # -> Se não existe (não foi digitada) ele retorna como Zero.

'''Função | Ler o texto antes de executar o programa'''
def solicitar_texto() -> str:
    while True:
        # Texto do usuário
        txt = input("Digite um texto: \n").strip()
        
        # Garantir que o usuário não deixe o conteudo vazio ou apenas com espaços.
        if txt == "":
            print('Erro: O texto não pode ser vazio, digite novamente.\n')
            continue

        # Garantir que o usuário digite ao menos uma letra.
        if not texto_tem_letra(txt):
            print('Erro: O texto precisa ter pelo menos uma letra, digite novamente.\n')
            continue
        return txt
    
'''Função | Bloquear o texto que não possui letras.'''
def texto_tem_letra(txt: str) -> bool:
    return any(ch.isalpha() for ch in txt)

'''Função | Check List'''
def validar_texto(txt: str) -> None:
    vazio = (txt.strip() == "")
    tem_letra = any(ch.isalpha() for ch in txt)
    print("Checklist de validação:")
    print(f"• Texto não está vazio...: {'✅' if not vazio else '❌'}")
    print(f"• Texto possui letras....: {'✅' if tem_letra else '❌'}")

# ================================================================================= #
# Menu do Programa                                                                  #
# ================================================================================= #
if __name__ == "__main__":

    # Entrada
    txt_usuario = solicitar_texto()                     

    # Processamento
    cont_por_vogal = contagem_por_vogal(txt_usuario)    
    total = sum(cont_por_vogal.values())

    # Saída
    print('=================================================================')
    print('Contador de Vogais'.center(65))
    print('=================================================================')
    validar_texto(txt_usuario)
    print('=================================================================')
    print('Resumo:')
    print(f'• Texto digitado......: {txt_usuario}')
    print(f'• Total de vogais.....: {total}')
    print('• Detalhe por vogal...: ')
    for v in "aeiou":
        print(f'   - {v}: {cont_por_vogal[v]}')
    print('=================================================================')
    print('Programa encerrado com sucesso.')
    print('=================================================================')

# Autor......: Diego Noberto Diniz
# GitHub.....: https://github.com/NbDiego
# Projeto....: Contagem de vogais em um texto

# Criado em..: 26/12/2025
