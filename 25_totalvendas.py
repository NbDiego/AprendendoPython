# Praticando Python | 025 | Código | Faça como eu fiz: calculando o total de vendas

# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. 
# As vendas são informadas em uma única linha separadas por espaços.
# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

# Racional
# Entrada       - Receber uma linha com valores separados por espaço (ex.: "10.50 20.00 5.75").
# Processamento - Converter para números.
# Saida         - Somar e exibir o total.

# ===================================================================================== #
# Entrada | Interação com o usuário                                                     #
# ===================================================================================== #

'''Função | Receber os valores'''
def ler_vendas():
    linha = input("Digite os valores das vendas separados por espaço: ").strip()
    if not linha:
        print("Atenção! Você não informou nenhum valor, por favor, digite novamente.")
        return []
    return linha.split() # Quebra a string em lista: ["10.50", "20.00", "5.75"]

# ===================================================================================== #
# Processamento                                                                         #
# ===================================================================================== #

'''Função | Trocar a virgula por ponto'''
# A ideia aqui é tratar o valor caso a pessoa digite 10,50 ao inves de 10.50
def ajustar_decimal(valor_str: str) -> str:
    # Remove espaços e troca vírgula por ponto (ex.: "10,50" -> "10.50")
    return valor_str.strip().replace(",", ".")

'''Função | Converte para float'''
def converter_para_float(lista):
    convertidos = []
    erros = []
    for i, v in enumerate(lista, start=1):
        v_norm = ajustar_decimal(v)
        try:
            convertidos.append(float(v_norm))
        except ValueError:
            erros.append((i, v))  # guarda posição e valor original inválido
    return convertidos, erros

'''Função | Soma todos os valores'''
def calcular_total(lista):
    return sum(lista) if lista else 0.0

# ===================================================================================== #
# Saída                                                                                 #
# ===================================================================================== #

'''Função | Formata número no padrão pt-BR: milhar com ponto e decimal com vírgula.'''
def br_moeda(x: float) -> str:
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

'''Função | Total com formatação. '''
def exibir_total(total: float):
    print(f"Total de vendas: R$ {br_moeda(total)}")

'''Função | Relatório Contábil.'''
def exibir_relatorio(valores):
    if not valores:
        print("Não há valores válidos para relatório.")
        return

    qtd = len(valores)
    total = sum(valores)
    media = total / qtd
    menor = min(valores)
    maior = max(valores)

    print(f"Itens válidos: {qtd}")
    print(
        f"Total: R$ {br_moeda(total)} | "
        f"Média: R$ {br_moeda(media)} | "
        f"Menor: R$ {br_moeda(menor)} | "
        f"Maior: R$ {br_moeda(maior)}"
    )
# Racional do Relatório
# De forma simples, quero exibir um relatório contábil com:
# 1 - quantidade de itens válidos
# 2 - total
# 3 - média
# 4 - menor valor
# 5 - maior valor
# ===================================================================================== #
# Formulário Principal                                                                  #
# ===================================================================================== #
if __name__ == "__main__":
    vendas = ler_vendas()
    vendas_convertidas, erros = converter_para_float(vendas)

    if erros:
        print("Atenção: alguns itens não foram convertidos:")
        for pos, val in erros:
            print(f"  - Posição {pos}: '{val}' (inválido)")

    total = calcular_total(vendas_convertidas)
    exibir_total(total)
    exibir_relatorio(vendas_convertidas)