# Calculando a gorjeta em um restaurante

# João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.
# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.
# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

# Importa a classe datetime
from datetime import datetime

# ================================================================================= #
# DATETIME                                                                          #
# ================================================================================= #
# Obter dia e horario                                                               #
# ================================================================================= #
# Obtém data e hora atuais
agora = datetime.now() 

# Formata a data (dia/mês/ano)
data_formatada = agora.strftime("%d/%m/%Y")  

# Formata a hora (hora:minuto:segundo)
hora_formatada = agora.strftime("%H:%M:%S") 

# ================================================================================= #
# Funções do Programa                                                               #
# ================================================================================= #

'''Função | Tratar Percentual'''
def tratar_percentual(msg: str) -> int:
    while True:
        txt = input(msg)

        # Regra de Tratamento do dado: Remove espaços 
        txt = txt.strip()
        if len(txt) == 0:
            print('Erro: campo vazio. Digite um inteiro entre 0 e 100 (ex.: 10, 13, 18).')
            continue

        # Regra de Tratamento do dado: Não aceitar espaços vazios
        if ' ' in txt:
            print('Erro: não use espaços vazios.')
            continue

        # Regra de negócio: Máximo 3 caracteres totais
        if len(txt) > 3:
            print('Erro: porcentagem deve ter no máximo 3 caracteres (ex.: 9, 10, 100).')
            continue

        # Regra de negócio: Não aceitar vírgula ou ponto
        if ',' in txt or '.' in txt:
            print('Erro: a porcentagem deve ser inteira, sem vírgula ou ponto (ex.: 10, 13, 18).')
            continue

        # Regra de negócio: Apenas dígitos (0–9)
        if not txt.isdigit():
            print('Erro: digite apenas números inteiros (ex.: 10, 13, 18).')
            continue

        # Converte para int
        valor = int(txt)

        # Regra de negócio: Converte e valida intervalo
        if valor < 0:
            print('Erro: a porcentagem não pode ser negativa.')
            continue
        if valor > 100:
            print('Erro: a porcentagem não pode ser superior a 100.')
            continue

        # Passou em todas as validações
        return valor

'''Função | Tratar Valor da Conta'''
def tratar_valor_conta(msg: str) -> float:
    while True:
        txt = input(msg)

        # Regra de Tratamento do dado: Remove espaços
        txt = txt.strip()

        # Regra de Tratamento do dado: Não aceitar espaços vazios
        if len(txt) == 0:
            print('Erro: digite um valor numérico (ex.: 130 ou 130,99).')
            continue

        # Regra de Tratamento do dado: Não aceitar espaços internos (ex.: '1 20')
        if " " in txt:
            print('Erro: não use espaços no meio (ex.: 120 50).')
            continue

        # Regra de Tratamento do dado: Aceitar a vírgula -> ponto para conversão
        normalizado = txt.replace(",", ".")

        # Regra de negócio: Tentar converter o texto para float
        try:
            valor = float(normalizado)
        except ValueError:
            print('Erro: valor inválido. Use apenas números (ex.: 130 ou 130,99).')
            continue

        # Regras de negócio: = 0 | Não pode ser igual a zero
        if valor == 0:
            print('Erro: o valor da conta não pode ser igual a zero.')
            continue

        # Regras de negócio: Não pode ser um número negativo ou igual a Zero
        if valor <= 0:
            print('Erro: o valor da conta deve ser MAIOR que zero.')
            continue

        # Tudo certo
        return valor

'''Função | Formatar valores em Reais'''
def formatar_brl(valor: float) -> str:
    # Formata como '1,234.56' (padrão US)
    s = f"{valor:,.2f}"
        # ,   → adiciona separador de milhares usando o padrão “US” (vírgula para milhar).
        # .2f → formata como número de ponto flutuante com 2 casas decimais.

    # Troca para '1.234,56' (padrão BR)
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
        # 1º s.replace(",", "X")
        # Troca vírgula por X 
        # Exemplo: De 1,234.56. Para 1X234.56
        # -----------------------------------------
        # 2º .replace(".", ",")
        # Troca ponto por vírgula
        # Exemplo: De 1X234.56 Para 1X234,56
        # -----------------------------------------
        # 3º .replace("X", ".")
        # Troca o marcador X por ponto
        # Exemplo: De 1X234.56 Para 1.234,56

    # Tudo certo
    return f"R$ {s}"

# ================================================================================= #
# Menu do Programa                                                                  #
# ================================================================================= #
if __name__ == "__main__":
    # Entrada
    valor_da_conta = tratar_valor_conta('\nDigite o valor da sua conta: \n')
    valor_do_servico = tratar_percentual('\nSugerimos 10% para gorjeta, digite a porcentagem que gostaria de pagar: \n')

    # Processamento
    valor_da_gorjeta = valor_da_conta * (valor_do_servico / 100)
    valor_total = valor_da_conta + valor_da_gorjeta

    # Saída | Recibo para o cliente
    print('\n=================== ALURA BURGUER ===================')
    print('                       Osasco                        ')
    print('=====================================================')
    print(f'Impresso em {data_formatada} às {hora_formatada}')
    print('')
    print('       *** Este não é um documento fiscal ***       ')
    print('')
    print('=====================================================')
    print('Serviço do restaurante:')
    print(f'Taxa de serviço.......: {valor_do_servico:>26} %')
    print(f'Valor da gorjeta......: {formatar_brl(valor_da_gorjeta):>28}')
    print('=====================================================')
    print('Total: ')
    print(f'+ Serviço.............: {formatar_brl(valor_da_gorjeta):>28}')
    print(f'+ Valor da compra.....: {formatar_brl(valor_da_conta):>28}')
    print(f'= Total a Pagar.......: {formatar_brl(valor_total):>28}')
    print('=====================================================')
    print('Obrigado por usar o Alura Burguer!')
    print('Programa encerrado com sucesso.')
    print('=====================================================\n')

    # Autor......: Diego Noberto Diniz
    # GitHub.....: https://github.com/NbDiego
    # Projeto....: Calculadora de Gorjeta
    # Criado em..: 26/12/2025