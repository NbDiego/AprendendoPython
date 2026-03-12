# Projeto | Pedra, papel e tesoura

# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. 

# ================================================================================= #
# Biblioteca Python                                                                 #
# ================================================================================= #

import random   # Gerar números aleatórios
import time     # Módulo de tempo

# ================================================================================= #
# Funções do Programa                                                               #
# ================================================================================= #

'''Função | Jogada do usuário'''
def obter_escolha_usuario() -> str:

    # Opções válidas
    opcoes_validas = ['pedra', 'papel', 'tesoura']
    
    # Primeira leitura
    escolha = input("Faça sua jogada:\n").strip().lower()
    
    # Validação em loop
    while escolha not in opcoes_validas:
        print("\n ❌ Jogada inválida!\n")
        escolha = input("Faça sua jogada, escolha entre: Pedra, Papel ou Tesoura.\n").strip().lower()
    
    return escolha

'''Função | Jogada do computador'''
def obter_escolha_computador() -> str:
    # Gera uma escolha aleatória entre as três opções
    return random.choice(['pedra', 'papel', 'tesoura'])

'''Função | Decide o vencedor'''
def decidir_vencedor(jogador: str, computador: str) -> str:

    if jogador == computador:
        return 'empate'
    
    # Quem vence quem 
    vence = {
        'pedra': 'tesoura',   # Pedra quebra Tesoura
        'papel': 'pedra',     # Papel cobre Pedra
        'tesoura': 'papel'    # Tesoura corta Papel
    }
    
    if vence[jogador] == computador:
        return 'jogador'
    else:
        return 'computador'

'''Função | Narrador sombrio'''
def narrador(msg: str, pausa: float = 1.2):
    # texto que será exibido
    print(f" 😈  {msg}")

    # tempo (em segundos) antes de continuar
    time.sleep(pausa)

# ================================================================================= #
# Menu do Programa                                                                  #
# ================================================================================= #
if __name__ == "__main__":
    # Entrada
    print('')
    print('=' * 50)
    print(' ✊ Pedra | ✋ Papel | ✌️  Tesoura '.center(50))
    print('=' * 50)
    print('Regras do Jogo:')
    print('-' * 50)
    print('Opção       | Vence        | Jogada ')
    print('-' * 50)
    print(' ✊ Pedra   | ✌️  Tesoura   | Pedra quebra Tesoura')
    print(' ✋ Papel   | ✊  Pedra     | Papel cobre Pedra')
    print(' ✌️ Tesoura | ✋  Papel     | Tesoura corta Papel')
    print('=' * 50)
    print("\n 😈  Vamos jogar um jogo?")
    print('')
    print('A escolha é simples… sobreviver, ou não.\n')

    # Jogada do Usuário
    escolha = obter_escolha_usuario()
    print('')
    narrador("Hmm... que jogada interessante.", pausa=1.5)
    print('')
    narrador("Agora é a vez do computador jogar...", pausa=1.5)

    # Jogada do Computador
    escolha_pc = obter_escolha_computador()
    print('')
    narrador("Decisão tomada.", pausa=1.5)
    print('')
    narrador("O destino foi selado...", pausa=1.8)
    print('')
    print('-' * 50)
    print(f'Você jogou.........: {escolha}')
    print(f'Computador jogou...: {escolha_pc}')
    print('-' * 50)

    # Processamento
    resultado = decidir_vencedor(escolha, escolha_pc)
    print('')
                                 
    # Saída
    if resultado == 'empate':
        print(' 🤝 Empate!')
    elif resultado == 'jogador':
        print(' 🏆 Você venceu!')
    else:
        print(' 💀 Computador venceu!')
    print('')
    print("=" * 50)
    narrador('Jogo encerrado!')   
    print("=" * 50)

# Autor......: Diego Noberto Diniz
# GitHub.....: https://github.com/NbDiego
# Projeto....: Calculadora de Gorjeta
# Criado em..: 26/12/2025    