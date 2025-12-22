# Praticando Python | 006 | Código | Controle de acesso ao escritório

# Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.

'''Obter Horario'''
horario_usuario = int(input("Digite a hora atual (formato 24 horas): "))

'''Validar Horario'''
if 8 <= horario_usuario <= 18:
    print("Acesso liberado.")
elif horario_usuario < 8:
    print("Acesso negado! O escritório só permite acesso entre 8h e 18h.")
elif horario_usuario > 18:
    print("Acesso negado! O escritório só permite acesso entre 8h e 18h.")