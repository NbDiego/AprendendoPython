# Praticando Python | 008 | Código | Calculando pedágio

# Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:
# Até 100 km: R$ 10,00
# Entre 100 km e 200 km: R$ 20,00
# Acima de 200 km: R$ 30,00
# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

'''Essa função recebe um parâmetro msg (a mensagem que aparecerá no input) e retorna um int.'''
# A ideia dessa função é auxiliar na validação do valor, estou excluindo valores negativos e valor = zero.
def km_pedagio (msg: str) -> int:
    distancia = int(input(msg))
    while distancia <= 0:
        if distancia == 0:
            print("Erro: A distnância não pode ser igual a zero. Digite novamente.")
        elif distancia <0:
            print("Erro: A distnância não pode ser negativa. Digite novamente.")
        distancia = int(input(msg))
    return distancia
# o while só será executado se a condição for verdadeira, do contrario ele não entra na verificação.

'''Obter a distância do usuario'''
distancia = km_pedagio('Digite qual a distância a ser percorrida (em km): ')

'''Apresentar Resultado'''
if distancia <= 100:
    print(f'Para a distância de {distancia} km, você vai gastar R$ 10,00 com pedágio!')
elif 100 < distancia <= 200:
    print(f'Para a distância de {distancia} km, você vai gastar R$ 20,00 com pedágio!')
elif distancia > 200:
    print(f'Para a distância de {distancia} km, você vai gastar R$ 30,00 com pedágio!')
# Os valores estão Definidos no execicio, portanto, basta fazer a condição por valor.