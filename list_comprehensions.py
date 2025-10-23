"""
Criar uma lista com a media dos estudantes de uma lista de listas, que foram criadas na situação.
Cada lista de listas possui as 3 notas de cada estudante"""


notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float: # função para calcular media passadas por uma lista
    ''' Função para calcular a média de notas passadas por uma lista

    lista: list, default [0]
        Lista com as notas para calcular a média
    return = calculo: float
        Média calculada
    '''     
    
    calculo = sum(lista) / len(lista)
    return calculo

# Agora vem a list comprehenssion - [expressao for item in lista]

medias = [round(media(nota),1) for nota in notas]

# print(medias)

