"""Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares 
e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e 
devolva o valor em reais do quanto precisará pagar.

Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de:
 A = π*r^2 (lê-se pi vezes raio ao quadrado).
"""

from math import pow, pi
raioCircular = int(input("Escreva o tamanho em metros do raio da área circular: "))

area = pi * pow(raioCircular, 2)

valorMonetario = area * 25

print(f"o Valor total será R${round(valorMonetario, 2)} para plantar grama em uma área de {round(area, 2)} metros quadrados")
