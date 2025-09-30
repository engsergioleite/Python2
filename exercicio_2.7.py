"""Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante 
concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

O texto exibido ao fim deve ser parecido com:

"Nome completo: Ana Silva"

"""

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]


#vamos colocar o metodo .capitalize() ou .title() diretamente na função para entregar a lista ajustada.
nomeSobrenome = list(map(lambda nome, sobrenome: nome.capitalize() + " " + sobrenome.title(), nomes, sobrenomes))

print(nomeSobrenome)