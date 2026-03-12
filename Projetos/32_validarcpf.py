# Projeto | Validar CPF

# O CPF deve conter exatamente 11 dígitos numéricos.
# Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.

# ================================================================================= #
# Funções do Programa                                                               #
# ================================================================================= #

'''Função | Limpar espaços'''
def limpar_espacos(texto: str) -> str:
    # Remover espaços nas extremidades
    texto_sem_espacos_pontas = texto.strip()       

    # Remover espaços internos
    texto_sem_espacos_total = texto_sem_espacos_pontas.replace(" ", "")  

    # Tudo Certo
    return texto_sem_espacos_total

'''Função | Retorna True se o texto estiver vazio'''
def nulo_vazio(texto: str) -> bool:
    return texto == ""

'''Função | Retorna True se TODOS os caracteres forem dígitos (0–9).'''
def somente_numero(texto: str) -> bool:
    return texto.isdigit()

'''Função | Mensagem de Erro'''
def mostrar_mensagem_erro(erro: str) -> None:
    print(f'Erro: {erro}\n')

'''Função | Retorna True se todos os dígitos forem iguais | Exemplo 00000000000'''
def todos_digitos_iguais(cpf: str) -> bool:
    return len(cpf) > 0 and cpf == cpf[0] * len(cpf)

# ================================================================================= #
# Menu do Programa                                                                  #
# ================================================================================= #
if __name__ == "__main__":
    while True:
        # Entrada
        numero_cpf = input('Digite o número do CPF com 11 dígitos e sem caracteres:\n')

        # Processamento
        # 1º Limpar espaços em Branco
        cpf_limpo = limpar_espacos(numero_cpf)

        # 2º Verificar se está vazio
        if nulo_vazio(cpf_limpo):
            mostrar_mensagem_erro('A entrada está vazia.')
            continue

        # 3º Verificar se os caracteres são dígitos (0–9).
        if not somente_numero(cpf_limpo):
            mostrar_mensagem_erro('O CPF deve conter apenas números (sem letras, pontos ou símbolos).')
            continue

        # 4º Verificar se o CPF tem 11 caracteres
        cpf_tamanho = len(cpf_limpo)
        if cpf_tamanho != 11:
            if cpf_tamanho < 11:
                mostrar_mensagem_erro(f'Você digitou {cpf_tamanho} números (faltam {11 - cpf_tamanho}).')
            else:
                mostrar_mensagem_erro(f'Você digitou {cpf_tamanho} números (retire {cpf_tamanho - 11} dígito(s)).')
            continue

        # 5 º Garantir que o número não seja duplicado, exemplo: 00000000000
        if todos_digitos_iguais(cpf_limpo):
            mostrar_mensagem_erro('CPF inválido — todos os dígitos são iguais')
            continue

        # Se passou por todas as regras desta etapa, encerramos a leitura
        break

        # Saída | Checklists simples
print('')
print('============================================')
print('Validador de CPF')
print('============================================')
print('Resumo das validações:')
print(f"• {'Limpeza do campo':<35} {'✅':>3}")
print(f"• {'Sem espaço vazio':<35} {'✅':>3}")
print(f"• {'Apenas números':<35} {'✅':>3}")
print(f"• {'Tamanho exato (11 dígitos)':<35} {'✅':>3}")
print(f"• {'Não são todos os dígitos iguais':<35} {'✅':>3}")
print('============================================')
print(f"O CPF {cpf_limpo} é válido!")
print('============================================')
print('Programa encerrado com sucesso.')
print('============================================\n')

# Autor......: Diego Noberto Diniz
# GitHub.....: https://github.com/NbDiego
# Projeto....: Validar CPF

# Criado em..: 26/12/2025
