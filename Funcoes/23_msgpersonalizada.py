# Praticando Python | 023 | Código | Faça como eu fiz: contador de caracteres

# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:
# Se for antes das 12h, exibir "Bom dia";
# Entre 12h e 18h, exibir "Boa tarde";
# Após 18h, exibir "Boa noite".

'''Função | Validar Horario'''
def ler_hora(msg: str) -> int:
    # laço infinito
    while True:
        # .strip() para remover espaços
        entrada = input(msg).strip()
        try:
            hora = int(entrada)
            if 0 <= hora <= 23:
                return hora
            print('Erro: É importante que você informe uma hora entre 0 e 23.')
        except ValueError:
            print('Erro: Por favor, digite apenas números inteiros para a hora.')

'''Função | Definir a saudação'''
def saudacao_por_hora(hora: int) -> str:
    # Classificação de horario
    if hora < 12:
        return "Bom dia"
    elif hora <= 18:
        return "Boa tarde"
    else:
        return "Boa noite"

'''Função | Personalizada | Melhorar experiencia com o usuário'''
def escolher_tratamento() -> str:
    # Uso de Dicionário para que a pessoa possa escolher como ela deseja ser tratada
    opcoes = {
                "1": "Sr.",
                "2": "Sra.",
                "3": "Sr(a).",
                "4": "Sem tratamento",
                "5": "Outro (personalizar)"
            }

    print("\nComo você prefere ser tratado(a)?")
    for k, v in opcoes.items():
        print(f"{k} - {v}")
        # {k} = chave do dicionário
        # {v} = valor do dicionário

    # laço infinito 
    while True:
        # Opção de escolha
        escolha = input("Escolha uma opção (1-5): ").strip()

        # Verificar se a chave digitada (escolha) existe no dicionário (opcoes)
        if escolha in opcoes:
            # A opção 4 é um escolha de sem tratamento, então chamamos apenas pelo nome
            if escolha == "4":
                return ""  
            # A opção 5 é personalizada, então vamos obter essa informação do usuário
            elif escolha == "5":
                personal = input("Digite a forma de tratamento desejada (ex.: Prezade, Menine, etc.): ").strip()
                return personal
            else:
                return opcoes[escolha]
        # Erro: Se o que você escolheu no dicionário não for valido, vai sair aqui
        # Aqui como estamos dentro do laço infinito, ele vai mostrar a mensagem e recomeçar o processo.
        print("Opção inválida. Tente novamente.")

'''Função | Menu Principal do app'''
def main():
    # Chamar a função do Nome
    nome = input("Digite seu nome: ").strip()
    # Chamar a função do horario
    hora = ler_hora("Digite a hora (0 a 23): ")
    # Chamar a função de tratamento
    tratamento = escolher_tratamento()

    # O resultado do texto (bom dia, boa tarde, boa noite) guardo em cumprimento
    cumprimento = saudacao_por_hora(hora)
    
    # Montar a mensagem combinando o Nome, hora e tratamento
    if tratamento:
        mensagem = f"{cumprimento}, {tratamento} {nome}!"
    else:
        mensagem = f"{cumprimento}, {nome}!"

    print(mensagem)

if __name__ == "__main__":
    main()