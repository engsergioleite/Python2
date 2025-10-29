"""
Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas 
de um estudante.

Caso o(a) estudante não esteja matriculado(a) na turma devemos tratar a exceção para aparecer a mensagem 
"Estudante não matriculado(a) na turma".

Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço do código.

Vamos testar esse primeiro tratamento?"""

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0], 
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

"""
try:
  # código a ser executado. Caso uma exceção seja lançada, pare imediatamente
except <nome_da_excecao as e>:
  # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa"""

try:
    nome = input("Escreva o nome para ler a nota: ")
    resultado = notas[nome]
    print(resultado)
except KeyError:
    print("Nome digitado não existe")

# Try, except e else

"""
Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas
de um estudante.

Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a
mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a
lista com as notas do(a) estudante.

Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço 
do código.

Vamos testar esse tratamento?"""

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0], 
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
    nome = input("Escreva o nome para ler a nota: ")
    resultado = notas[nome]
except KeyError:
    print("Nome digitado não matriculado na turma")
else:
    print(resultado)


# Agora usando o finally
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0], 
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
    nome = input("Escreva o nome para ler a nota: ")
    resultado = notas[nome]
except KeyError:
    print("Nome digitado não matriculado na turma")
else:
    print(resultado)
finally:
    print("Obrigado pela tentativa!")