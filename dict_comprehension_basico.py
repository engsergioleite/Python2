#Forma manual
"""numeros = [1, 2, 3, 4, 5]
quadrados = {}
for num in numeros:
    quadrados[num] = num ** 2
print(quadrados)
"""
# Usando dict comprehension
numeros = [1, 2, 3, 4, 5]
novoDicionario = {num: num**2 for num in numeros}
print(novoDicionario)


# usando dict conprehension com IF
numeros2 = [1, 2, 3, 4, 5, 6, 7]
novaDict = {num: num ** 2 for num in numeros2 if num % 2 == 0}
print(novaDict)

# com um dicionario já existente
frutas_e_cores = {
    "banana": "amarela",
    "maçã": "vermelha",
    "uva": "roxa",
    "limão": "verde"
}
tamanho_por_fruta = {
    len(fruta): fruta          # A chave é o len(fruta), o valor é a 'fruta' (chave antiga)
    for fruta, cor in frutas_e_cores.items() # Itera sobre chave E valor do dicionário
}

print(tamanho_por_fruta)

"""Seu Desafio: Tente criar um dicionário a partir da seguinte lista de palavras, onde a chave é a 
palavra e o valor é a palavra em maiúsculas, mas somente se a palavra tiver mais de 4 letras."""

palavras = ["sol", "lua", "estrela", "terra", "marte"]
dictPalavras = {palavra: palavra.upper() for palavra in palavras if len(palavra) > 4}
print(dictPalavras)


#Transformar um dicionário de Capitais e Países em um onde o País é a Chave e a Capital é o Valor.
# dict comprehension com dicionario
capitais_paises = {
    "Brasília": "Brasil",
    "Paris": "França",
    "Madri": "Espanha"
}

novoDict = {pais: capital for capital, pais in capitais_paises.items()}

print(novoDict)


"""Recebemos uma demanda da instituição de ensino do nosso projeto que nos repassou uma lista de 20 
estudantes e suas respectivas médias finais. Aqui, nós precisamos selecionar estudantes que tenham média 
final maior ou igual a 9.0. Esses(as) estudantes serão premiados(as) com uma bolsa de estudos para o 
próximo ano letivo."""

nomes_estudantes = [ "Enrico Monteiro", "Luna Pereira", "Anthony Silveira", "Letícia Fernandes", 
                    "João Vitor Nascimento", "Maysa Caldeira", "Diana Carvalho", "Mariane da Rosa",
                    "Camila Fernandes", "Levi Alves", "Nicolas da Rocha", "Amanda Novaes", 
                    "Laís Moraes", "Letícia Oliveira", "Lucca Novaes", "Lara Cunha", 
                    "Beatriz Martins", "João Vitor Azevedo", "Stephany Rosa", "Gustavo Henrique Lima" ]

medias_estudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5,
                    8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 6.7, 8.2]

dictAlunos = bolsistas = {nome: media 
             for nome, media in zip(nomes_estudantes, medias_estudantes) 
             if media >= 9.0}

print(dictAlunos)