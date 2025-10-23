"""Situação 11:
Agora, a nossa demanda consiste em gerar um dicionário a partir da lista de listas que criamos na 
Situação 10 para passar para a pessoa responsável por construir as tabelas para a análise dos dados.

As chaves do nosso dicionário serão as colunas identificando o tipo de dado
Os valores serão as listas com os dados correspondentes àquela chave.
Vamos resolver esse desafio?

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.

Dica: Utilize o formato

{chave: valor for item in lista}"""

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]
# dicionario = {chave: valor for item in lista}

# colunas com os tipos de dados (exceto nome)
coluna = ["Notas", "Média final", "Situação"]

# Vamos por fim adicionar o nome dos estudantes, extraindo apenas seus nomes da lista de tuplas
cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))} #i+1 pois queriamos pular o nome e codigo, indo direto para notas

cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))] # inclusão do estudante separado, para nao incluir o codigo

print(cadastro)