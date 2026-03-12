# Praticando Python | 003 | Código | Temperatura dos servidores

# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

'''Obter a temperatura'''
temperatura = float(input("Digite a temperatura atual (sem o ºC): "))

if temperatura == 25:
    print(f"Atenção! A temperatura está em {temperatura}ºC, esse número está no limite permitido.")
elif temperatura > 25:
    print(f"Atenção! A temperatura está em {temperatura}ºC, esse número está acima do limite permitido.")
else:
    print(f"A temperatura está em {temperatura}ºC, estamos dentro do limite.")