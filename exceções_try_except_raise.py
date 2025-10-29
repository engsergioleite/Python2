"""
Você criou uma função para calcular a média de um estudante em uma dada matéria passando em uma lista 
as notas deste estudante.

Você pretende tratar 2 situações:

Se a lista possuir um valor não numérico o cálculo de média não será executado e uma mensagem de "Não 
foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!" será exibida.
Caso a lista tenha mais de 4 notas, será lançada uma exceção do tipo ValueError informando que "A 
lista não pode possuir mais de 4 notas."

Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada."""

def media(lista: list=[0]) -> float:
    ''' Função para calcular a média de notas passadas por uma lista

    lista: list, default [0]
        Lista com as notas para calcular a média
    return = calculo: float
        Média calculada
    '''
    calculo = sum(lista) / len(lista)
    if len(lista) > 4:
        raise ValueError("A Lista não pode possuir mais de 4 notas")
    return calculo

try:
    notas = [5.0, 7.0, 10.0, 8.0, 9.0]
    resultado = media(notas)
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")