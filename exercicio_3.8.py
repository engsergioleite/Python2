"""
Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos 
nas seguintes listas:

O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é 
obtida multiplicando a quantidade pelo preço unitário. 

Além disso, a tabela precisa conter um 
cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.

Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual 
a primeira tupla é o cabeçalho da tabela."""

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
total = [qtd * pre for qtd, pre in zip(quantidade, preco)]   
cabecalho = [("ID", "Quantidade", "Preço", "Total")]

listaTupla = [(i, q, p, t) for i, q, p, t in zip(id, quantidade, preco, total)]
print([cabecalho] + listaTupla)


#Solução proposta pela ALURA
tabela = [('id', 'quantidade', 'preco', 'total')]
tabela += [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]
print(tabela)