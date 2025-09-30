"""
Exercício 1: Dobrando Valores
Objetivo: Criar uma nova lista em que cada número da lista original é multiplicado por 2.

Lista inicial: numeros = [10, 20, 30, 40, 50]

Resultado esperado: [20, 40, 60, 80, 100]"""

numeros = [10, 20, 30, 40, 50]

dobraValores = map(lambda x: x * 2, numeros)

print(list(dobraValores))