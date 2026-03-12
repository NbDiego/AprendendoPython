# Praticando Python | 029 | Código | Faça como eu fiz: gerador de funções personalizadas

# Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
# Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

# Premissa | Função closure, é quando uma função interna usa variáveis da função externa e “guarda” esse contexto mesmo depois que a externa termina. 
# A função interna vai “lembrar” o desconto definido pelo usuário e usá-lo para calcular o preço final.

# Racional | Criar uma função que recebe o desconto fixo e gere outra função que aplica esse desconto em qualquer valor de compra.

# ===================================================================================== #
# ENTRADA | Funções auxiliares para leitura                                             #
# ===================================================================================== #

'''Função | Aceitar ponto ou vírgula'''
def ler_float(msg: str) -> float:
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print('Erro: Este número não é valido, tente algo como: 100.99.')

'''Função | valores em reais'''
def real_br(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ===================================================================================== #
# PROCESSAMENTO | Função Geradora (Closure)                                             #
# ===================================================================================== #

'''Função | Motor de Cálculo'''
def motor_de_desconto(desconto_percentual: float):
    # Validação do desconto: precisa estar entre 0% e 100%
    if not (0 <= desconto_percentual <= 100):
        raise ValueError('O desconto deve estar entre 0 e 100 (%).')

    # Converter o percentual em taxa decimal | 10% -> 0.10
    taxa = desconto_percentual / 100

    # Função interna (closure) que usa a taxa "lembrada" da função externa
    def aplicar_desconto(valor: float) -> float:
        # Validação: não permitir valores negativos
        if valor < 0:
            raise ValueError('Erro: Não é permitido valor de compra negativo.')
        # Cálculo do preço final: valor * (1 - taxa)
        return valor * (1 - taxa)

    # Retorna a função configurada com a taxa fixa (closure)
    return aplicar_desconto

# ===================================================================================== #
# SAÍDA | Executar e Mostrar o Resultado                                                #
# ===================================================================================== #

if __name__ == "__main__":
    print("======= Gerador de Preço com Desconto =======\n")

    # ENTRADA
    desconto_escolhido = ler_float('Digite a porcentagem de desconto: ')
    aplicar = motor_de_desconto(desconto_escolhido)  # gerar a função com a taxa fixa

    # Loop para permitir várias compras até o usuário sair
    while True:
        valor_compra = ler_float('\nDigite o valor da compra (ou 0 para sair): ')
        if valor_compra == 0:
            print("\nAté mais, bom trabalho!")
            break

        # PROCESSAMENTO
        preco_final = aplicar(valor_compra)

        # SAÍDA
        print("\n============= Resultado =============")
        print(f"Desconto escolhido: {desconto_escolhido:.2f}%")
        print(f"Valor da compra:    {real_br(valor_compra)}")
        print(f"Preço com desconto: {real_br(preco_final)}")