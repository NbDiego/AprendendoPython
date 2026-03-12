# Projeto | Gerador de senha segura

# Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial.

# Exiba a senha gerada

# ================================================================================= #
# Biblioteca Python                                                                 #
# ================================================================================= #

# Importa a classe datetime
from datetime import datetime

# Gera números aleatórios [criptografia], ideal para senhas, tokens e chaves
import secrets

# Conjuntos prontos de caracteres
import string
# ---> string.ascii_uppercase -> "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ---> string.ascii_lowercase -> "abcdefghijklmnopqrstuvwxyz"
# ---> string.digits -> "0123456789"

# Tipagem: ajuda a indicar que uma lista contém strings
from typing import List

# ================================================================================= #
# Funções do Programa                                                               #
# ================================================================================= #

# Obtém data e hora atuais
agora = datetime.now() 

# Formata a data (dia/mês/ano)
data_formatada = agora.strftime("%d/%m/%Y")  

# Formata a hora (hora:minuto:segundo)
hora_formatada = agora.strftime("%H:%M:%S")

'''Função | Validar senha gerada'''
def validar_senha(senha: str) -> dict:
    """Retorna um dicionário indicando se cada requisito foi atendido."""
    has_upper = any(ch.isupper() for ch in senha)
    has_lower = any(ch.islower() for ch in senha)
    has_digit = any(ch.isdigit() for ch in senha)
    especiais = set("!@#$%^&*()-_=+[]{};:,.?/")
    has_special = any(ch in especiais for ch in senha)

    return {
        "Maiúscula": has_upper,
        "Minúscula": has_lower,
        "Número": has_digit,
        "Especial": has_special,
        "Tamanho ≥ 12": len(senha) >= 12,
    }

'''Função | Gerar Senha'''
def gerar_senha(tamanho: int = 12) -> str:
    # 4 Categorias: maiúscula, minúscula, número e caractere especial
    if tamanho < 4:
        raise ValueError('O tamanho mínimo precisa ser 4 para cumprir todos os requisitos.')

    # Premissa | Conjuntos de caracteres 
    letras_maiusculas = string.ascii_uppercase  # ABC...
    letras_minusculas = string.ascii_lowercase  # abc...
    digitos = string.digits                     # 0123456789
    especiais = "!@#$%^&*()-_=+[]{};:,.?/"

    # Criar uma lista para senha, obter um caractere de cada categoria
    senha: List[str] = [
        secrets.choice(letras_maiusculas),
        secrets.choice(letras_minusculas),
        secrets.choice(digitos),
        secrets.choice(especiais),
    ]

    # Preencher o restante com um pool (conjunto de opções) de todos os tipos
    pool = letras_maiusculas + letras_minusculas + digitos + especiais
    for _ in range(tamanho - len(senha)):
        senha.append(secrets.choice(pool))

    # Embaralhar caracteres para não gerar uma senha previsível
    secrets.SystemRandom().shuffle(senha)

    # Senha gerada
    return "".join(senha)

# ================================================================================= #
# Menu do Programa                                                                  #
# ================================================================================= #
if __name__ == "__main__":
    # Entrada
    tamanho_senha = 12  # Sem interação com o usuário neste caso!

    # Processamento
    senha_gerada = gerar_senha(tamanho=tamanho_senha)
    checklist = validar_senha(senha_gerada)

    # Saída
    print("=" * 38)
    print('Password System'.center(38))
    print("=" * 38)
    print("Senha:")
    print(senha_gerada)
    print("=" * 38)
    print(f'Senha gerada {data_formatada} às {hora_formatada}') 
    print("=" * 38)

    # Resumo das validações com ✅ (largura automática para alinhamento)
    print('Resumo das validações:')
    largura = max(len(nome) for nome in checklist.keys()) + 2  # +2 para folga
    for nome, ok in checklist.items():
        status = "✅" if ok else "❌"
        # • Nome do requisito alinhado à esquerda com largura fixa
        print(f'• {nome:<{largura}} {status}')

    print("=" * 38)
    print('Programa encerrado com sucesso.')   
    print("=" * 38)

# Autor......: Diego Noberto Diniz
# GitHub.....: https://github.com/NbDiego
# Projeto....: Calculadora de Gorjeta
# Criado em..: 26/12/2025 