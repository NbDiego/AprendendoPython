# Praticando Python | 007 | Código | Classificando estudantes por média

# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:
# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

'''Obter Notas do Aluno '''
nota_1 = float(input('Digite a 1º Nota: '))
nota_2 = float(input('Digite a 2º nota: '))
nota_3 = float(input('Digite a 3º nota: '))

'''Calcular a Média do Aluno'''
media = (nota_1 + nota_2 + nota_3) / 3

'''Classificar a Média'''
if media >= 7:
    print(f'Aluno aprovado com a média {media}')
elif 5 <= media < 7:
    print(f'Aluno está de Recuperação, sua média foi de {media}!')
else:
    print(f'Aluno foi Reprovado, sua média é de {media}!')