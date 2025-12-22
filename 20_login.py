# Praticando Python | 020 | Código | Validação de entrada para login

# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:
# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.
# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".
# Crie um programa que implemente essa lógica usando um laço while.

'''Criar função para valirdar o nome de usuário'''
def validar_nome_usuario(nome: str) -> bool:
    # Retorna True se o nome tiver pelo menos 5 caracteres.
    return len(nome) >= 5

'''Criar função para valirdar a senha do usuário'''
def validar_senha(senha: str) -> bool:
    # Retorna True se a senha tiver pelo menos 8 caracteres.
    return len(senha) >= 8

'''Criar função para cadastrar o usuário'''
def cadastrar():
    while True:
        nome = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if not validar_nome_usuario(nome):
            print("O nome de usuário deve ter pelo menos 5 caracteres.")
            continue

        if not validar_senha(senha):
            print("A senha deve ter pelo menos 8 caracteres.")
            continue

        print("Cadastro realizado com sucesso!")
        break

cadastrar()

# Racional
# O while True: vai manter o programa pedindo nome e senha eternamente.
# Ele só vai sair desse laço quando as condições forem atendidas.
# Por isso uso o break para interromper o laço e seguir para o final do programa.