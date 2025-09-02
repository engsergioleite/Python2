import math #importa a biblioteca e depois precisamos usar nomes completos para chamar os métodos

numero = int(input("Digite um número para calcular a raiz quadrada:"))
print(f"\nA raiz quadrade de {numero} é igual a: {math.sqrt(numero)}") #precisamos chamar a biblioteca math antes do método

"""
from math import *

numero = int(input("Digite um número para calcular a raiz quadrada:"))
print(f"\nA raiz quadrade de {numero} é igual a: {sqrt(numero)}") #usamos apenas o nome do método, sem chamar a biblioteca math antes, pois tudo foi importado no inicio.
"""
