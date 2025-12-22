# Praticando Python | 021 | Código | Faça como eu fiz: calculando a idade

# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

'''Função | verificar se o número é valido'''
def analisar_ano(msg: str) -> int:
    # While True é um loop infinito.
    while True:
        # O .strip() vai remover os espaços, imagine alguem digitando " 2025" ou "2025 ", ele ajusta para "2025"
        entrada = input(msg).strip()
        try:
            valor = int(entrada)
            # Se o número for zero ou negativo, não é valido.
            if valor <= 0:
                print('Erro! O ano deve ser um número inteiro positivo. Tente novamente.')
                continue

            # != 4 → Diferente de 4.
            # Aqui podemos ter um erro de digitação, exe.: 25
            if len(entrada) != 4:  
                print('Erro! informe o ano com 4 digitos, 2025.')
                continue

            # Se passou por todas as validações, aqui é o fim.
            return valor
    
        # ultima linha de desefa do codigo
        except ValueError:
            print('Erro! digite apenas números!')

# ----------------------------------------------------------------------------------------------------------------- #
# A ideia dessa função é garantir que não seja digitado texto ou número inválidos                                   #
# Se a pessoa tentar digitar número e texto, exe: 2o25 vai dar erro (ValueError) e o código pula para o except.     #
# ----------------------------------------------------------------------------------------------------------------- # 

'''Função | Calcular a idade'''
def sua_idade (aqe, adn: int) -> int:
    return aqe - adn

# ----------------------------------- # 
# aqe = Ano em que estamos | 2025     #
# adn = Ano de nascimento | 2005      #
# ----------------------------------- #

'''Obter os dados do usuario'''
AnoQueEstamos = analisar_ano("Digite o ano em que estamos: ")
AnoDeNascimento = analisar_ano("Digite o ano em que você nasceu: ")

'''Apresentar Resultado'''
idade = sua_idade(AnoQueEstamos, AnoDeNascimento)

if AnoDeNascimento > AnoQueEstamos:
    print("Erro: o ano de nascimento não pode ser maior que o ano atual.")
else:
    print(f"A sua idade é de {idade} anos.")