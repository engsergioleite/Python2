"""Escreva um código que lê a lista abaixo e faça:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

A leitura do tamanho da lista
A leitura do maior e menor valor
A soma dos valores da lista
Ao final exiba uma mensagem dizendo:

"A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. A soma dos 
valores presentes nela é igual a [soma]"""


lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

"""
for i in range(1, len(lista)):
    # Se o elemento atual for maior do que o 'maior' que temos até agora,
    # ele se torna o novo 'maior'.
    if lista[i] > maior:
        maior = lista[i]"""


#print(len(lista))
#print(sum(lista))
#print(max(lista))
#print(min(lista))


print(f"A lista possui {len(lista)} números em que o maior número é {max(lista)} e o menor número é {min(lista)}. A soma dos valores presentes nela é igual a {sum(lista)}")

print(map(lista, 1))