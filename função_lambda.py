"""nota = float(input("Digite a nota:"))

qualitativo = lambda x: x + 0.5
   
print(qualitativo(nota))
"""
"""# usando lambda

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

mediaPonderavel = lambda x, y, z: (x*3 + y*2 + z*5)/10  

mediaEstudante = mediaPonderavel(n1, n2, n3)

print(mediaEstudante)
"""
"""
# Usando lambda com a funcção MAP
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

notasAtualizadas = map(lambda x: x + qualitativo, notas)

print(list(notasAtualizadas))
"""
"""
Na aula de programação, a aluna Millena recebeu uma tarefa para 
converter uma lista de temperaturas de graus Celsius para Fahrenheit. 
Pesquisando sobre como realizar a conversão ela notou que era possível 
criar uma função lambda para converter as temperaturas, mas precisaria 
utilizar a função embutida map()para auxiliá-la na conversão elemento 
a elemento.

A conversão de temperaturas Celsius em Fahrenheit pode ser descrita da 
seguinte forma:

temp_fahrenheit = temp_celsius * 9/5 + 32"""

temp_celsius = [0, 25, 37, 78, 100]
temp_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temp_celsius))
print(temp_fahrenheit)