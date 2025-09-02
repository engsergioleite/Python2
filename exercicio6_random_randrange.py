"""Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede 
social para ganhar um prêmio. A lista de participantes é numerada e devemos 
escolher aleatoriamente um número de acordo com a quantidade de participantes. 
Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva
para ela o número sorteado."""


from random import randrange
print("SORTEIO")
print("\n")
qtdParticipante = int(input("Qual a quantidade de participantes do sorteio:"))
numSorteado = randrange(1, qtdParticipante)
print(f"O número de participantes foi {qtdParticipante} e o escolhido foi o {numSorteado}")
