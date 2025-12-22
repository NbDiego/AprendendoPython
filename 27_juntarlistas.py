# Praticando Python | 027 | Código | Faça como eu fiz: juntando listas de produtos

# Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
# Crie um programa que junte as listas e exiba o resultado no formato produto: preço


# ===================================================================================== #
# Entrada | Interação com o usuário                                                     #
# ===================================================================================== #
produtos = ["Camisa", "Calça", "Tênis"]
precos = [100.0, 120.0, 150.0]

# ===================================================================================== #
# PROCESSAMENTO | Combinar listas e preparar formatação                                 #
# ===================================================================================== #
'''Função | Formatar em Real (R$) com vírgula como separador decimal'''
def format_brl(valor: float) -> str:
    # formata com 2 casas e troca '.' por ',' 
    return f"R$ {valor:.2f}".replace('.', ',')

# Combina produto e preço em pares usando zip
pares_produto_preco = list(zip(produtos, precos))

# ===================================================================================== #
# SAÍDA | Exibir resultado                                                              #
# ===================================================================================== #
for produto, preco in pares_produto_preco:
    print(f"{produto}: {format_brl(preco)}")