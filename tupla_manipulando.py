# precisamos criar uma lista de tuplas onde o primeiro elemento é o nome e o segundo é a inicial do nome com o código
from random import randint # biblioteca responsável por criar numeros aleatorios

estudantes = ["João","Maria","José","Cláudia","Ana"]

def geraCodigo ():
    return str(randint(0, 999)) # o motivo para gerar em formato de string é que vai ser concatenado com a inicial do nome

codigoEstudante = []

# for para pegar o nome do estudante, a inicial do estudante [1][0] e concatenar com a string do codigo (função)
for i in range (len(estudantes)):
    codigoEstudante.append((estudantes[i], estudantes[i][0] + geraCodigo()))


print(codigoEstudante)

