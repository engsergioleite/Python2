"""
Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

Utilize o return na função e salve a nova lista na variável mult_3
"""

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]


def multiplo(listaNum: list) -> list: # list) -> list: - recebe uma lista e retorna uma lista
    mult_3 = []
    for numero in listaNum:
        if numero % 3 == 0:
            mult_3.append(numero)
    return mult_3

listaMult3 = multiplo(lista)

print(listaMult3)