from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(50))

lista2 = sample(lista, 5)

print(lista2)