"""
Recebemos duas demandas a respeito desse projeto com as notas dos estudantes:

Criar uma lista da situação dos estudantes em que caso se sua média seja maior ou igual a 6 receberá o 
valor "Aprovado" e caso contrário receberá o valor "Reprovado".
Gerar uma lista de listas com:
Lista de tuplas com o nome dos estudantes e seus códigos
Lista de listas com as notas de cada estudante
Lista com as médias de cada estudante
Lista da situação dos estudantes de acordo com as médias
Os dados que utilizaremos são os mesmos que geramos nas situações anteriores (nomes, notas, medias).

Vamos resolver esse desafio?

Para seguirmos o processo, vou deixar logo abaixo as estruturas de dados que já produzimos.

Dica: Para a lista das situações utilize o formato:

[resultado_if if cond else resultado_else for item in lista]"""

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

#criar a media de cada item da lista notas
"""def media(nota):
    media = sum(nota) / len(nota)
    return media
"""

# criar uma lista com aprovados e reprovados
situacao = ["Aptovado(a)" if media >= 6 else "Reprovado(a)" for media in medias]
print(situacao)

"""Gerar uma lista de listas com:
Lista de tuplas com o nome dos estudantes e seus códigos
Lista de listas com as notas de cada estudante
Lista com as médias de cada estudante
Lista da situação dos estudantes de acordo com as médias"""


# forma mais dificil
# cadastro = [alunos for alunos in [nomes, notas, medias, situacao]]

# forma pratica
cadastro = [nomes, notas, medias, situacao]
print(cadastro)
