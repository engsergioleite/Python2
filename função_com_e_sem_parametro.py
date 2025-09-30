# Função sem parametro 
"""
def media():
    calculo = (2 + 4 + 6 + 8)/4
    print(calculo) 

media()    
"""
"""
# com parametro

def media(n1, n2, n3, n4):
    calculo = (n1 + n2 + n3 + n4)/4
    print(calculo)

media(2, 4, 6, 8)
"""
"""
# com parametro e usando valores pelo argumento
def media(n1, n2, n3, n4):
    calculo = (n1 + n2 + n3 + n4)/4
    print(calculo)

n1 = 2
n2 = 4
n3 = 6
n4 = 8

media(n1, n2, n3, n4)
"""

"""
#funções com atribuição a variavel para mostrar o erro none ao atribuir a funcao em uma var fora do escopo
notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
    calculo = sum(lista) / len(lista)
    print(calculo)

resultado = media(notas)

print(resultado)
"""
"""
# Funções com retorno
notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
    calculo = sum(lista) / len(lista)
    return(calculo)

print(media(notas))
"""
"""
# Função retornando uma tupla 
notas = [8.5, 9.0, 6.0, 10.0]

def boletim(lista):
    calculo = sum(lista) / len(lista)
    if calculo >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return(calculo, situacao)


#print(boletim(notas))


# Atribuindo o valor do retorno para variaveis fora do escopo da função
media, situação = boletim(notas)
print(media)

print(situação)

# Ou

print(f"O Aluno recebeu a média {media} e foi {situação}")
"""

# Usando type hint

notas = [8.5, 9.0, 6.0, 10.0]

def media(lista: list=[0]) -> float:
    """
     Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
    """
    calculo = sum(lista) / len(lista)
    return calculo

help(media)
print(media(notas))

