"""
#### **Situação 9:**

Agora, precisamos utilizar as médias calculadas no exemplo anterior, pareando com o nome dos estudantes. 
Isto será necessário para gerar uma lista que selecione aqueles estudantes que possuam uma média final 
maior ou igual a 8 para concorrer a uma bolsa para o próximo ano letivo. Os dados recebidos correspondem
a uma lista de tuplas com os nomes e códigos dos estudantes e a lista de médias calculadas logo acima.

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.

**Dica:** Utilize o formato:
```python
[expr for item in lista if cond]
```
"""

nomes = [('João', 'J960'), ('Maria', 'M43'), ('José', 'J736'), ('Cláudia', 'C318'), ('Ana', 'A435')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

nome_nova = [nome[0] for nome in nomes] # agora temos uma lista apenas com os nomes e a lista medias com as menias de cada

estudantes = list(zip(nome_nova, medias))

candidatos = [aprovados[0] for aprovados in estudantes if aprovados[1] >= 7.0]
print(candidatos)