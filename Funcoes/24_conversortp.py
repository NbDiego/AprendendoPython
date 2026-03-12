# Praticando Python | 024 | Código | Faça como eu fiz: conversor de tipos

# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

'''Lista de telefones'''
telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

'''Função | Converter uma string para int (texto -> inteiro)'''
def converter_texto(lista):
    return [int(numero) for numero in lista]
    # int(numero):         Faz a conversão de texto para inteiro de cada item da lista.
    # for numero in lista: Ler item a item da lista de telefones. 

'''Função | Validar se o número de telefone é inteiro'''
def validar_numero(lista):
    if all(isinstance(numero, int) for numero in lista):
        return "Conversão foi executada com sucesso!"
    else:
        return "Conversão falhou! Há itens que não são inteiros."
    # isinstance(numero, int) = Vai retorna True se for do tipo int, se não for, reotrna False.
    # (for numero in lista)   = estou usando para produzir True/False para cada número de telefone da lista.
    # all(...)                = Só vai retorna True se todos os valores gerados forem True.

# Chama a função de conversão, criando uma nova lista com os telefones como inteiros.
telefones_convertidos = converter_texto(telefones)

# Exibir a nova lista
print("Convertidos:", telefones_convertidos)


# Mostrar a mensagem
mensagem = validar_numero(telefones_convertidos)
print(mensagem)