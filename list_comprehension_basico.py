# Básico [expressão for item in iterável]

numeros = [1, 2, 3, 4, 5]
quadrados = [num * num for num in numeros]
print(quadrados)

# Com IF [expressão for item in iterável if condição]

numeros_misto = [1, 2, 3, 4, 5, 6, 7, 8]
pares = [num for num in numeros_misto if num%2 == 0] # crias lista com pares
print(pares)

# com IF-ELSE [expressão_se_verdadeiro if condição else expressão_se_falso for item in iterável]
numeros_teste = [1, 2, 3, 4, 5]
numPar = []
numImpar = []

parOuImpar = [numPar.append(num) if num % 2 == 0 else numImpar.append(num) for num in numeros_teste]
print(f"os números pares são {numPar} e os impares são{numImpar}")
transformado2 = [numero * numero if numero % 2 == 0 else numero for numero in numeros_teste]
print(transformado2)