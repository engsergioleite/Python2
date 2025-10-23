notasTurma = ['João', 8.0, 9.0, 10.0, 
              'Maria', 9.0, 7.0, 6.0, 
              'José', 3.4, 7.0, 7.0, 
              'Claudia', 5.5, 6.6, 8.0, 
              'Ana', 6.0, 10.0, 9.5]

# Vamos transformar essa lista em uma lista simples, com os nomes separados das notas e ua lista de lista com as 3 notas de cada estudante separadas uma das outras

# primeiro vamos separar o nome das listas, analisando o padrão da lista e seus indices

nomes = []
notasJuntas = []
notas = []

for i in range(len(notasTurma)):
    if i % 4 == 0: #lógica utilizada de acordo com o padrão da lista, nesse caso, os nomes estavam nos indices 0, 4, 8, 12 e assim ficou facil separa-los
        nomes.append(notasTurma[i])
    else:
        notasJuntas.append(notasTurma[i])

# print(nomes)
# print(notasJuntas)

for i in range (0, len(notasJuntas), 3): 
    notas.append([notasJuntas[i], notasJuntas[i+1], notasJuntas[i+2]])


print(notas)
print(notas[2][2])

