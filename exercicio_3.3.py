"""
3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], 
crie um código para gerar uma lista de tuplas em que cada tupla tenha 
o primeiro elemento como a posição do nome na lista original e o segundo 
elemento sendo o próprio nome."""

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

listaCodigo = []
for i in range(len(lista)):
    listaCodigo.append([i])
listaFinal = list(zip(listaCodigo, lista))
print(listaFinal)

# Usando um metodo mais pratico
listaTupla = []
for i in range(len(lista)):
    listaTupla.append((i, lista[i]))
print(listaTupla)
