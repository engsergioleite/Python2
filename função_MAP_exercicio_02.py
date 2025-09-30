"""
Exercício 2: Formatando Nomes
Objetivo: Transformar uma lista de nomes em letras minúsculas para que a primeira letra de cada nome 
seja maiúscula.

Lista inicial: nomes = ['ana', 'luiz', 'carlos', 'sofia']

Resultado esperado: ['Ana', 'Luiz', 'Carlos', 'Sofia']"""

nomes = ['ana', 'luiz', 'carlos', 'sofia']

nomesInicialMaiuscula = list(map(lambda x: x.capitalize(), nomes))

print(nomesInicialMaiuscula)