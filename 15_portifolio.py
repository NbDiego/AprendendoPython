# Praticando Python | 015 | Código | Organizando seu portfólio

# Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens podem estar ausentes, aparecendo como None
# Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".

'''Lista de projetos'''
portifolio = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for nome_projeto in portifolio:
    if nome_projeto is None:
        print("Projeto ausente")
    else:
        print(nome_projeto)