"""Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais 
resultaram em um número inteiro. A lista é a seguinte:"""

from math import sqrt
numeros = [2, 8, 15, 23, 91, 112, 256, 256]
listaRaiz = []

for i in range(len(numeros)):
    listaRaiz.append(sqrt(numeros[i]))

for i in range(0, len(listaRaiz)):
    if listaRaiz[i] % 1 == 0:
        print(listaRaiz[i])
