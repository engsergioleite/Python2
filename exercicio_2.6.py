"""Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) 
estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

maior nota
menor nota
média
situação (Aprovado(a) ou Reprovado(a))
Para testar o comportamento da função, os dados podem ser exibidos em um texto:

"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota 
de [menor] pontos e foi [situacao]"""


notas = []
for i in range (0, 4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

def listaNotas(notas):
    maiorNota = max(notas)
    menorNota = min(notas)
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maiorNota} pontos e a menor nota de {menorNota} pontos e foi {situacao}")

listaNotas(notas)