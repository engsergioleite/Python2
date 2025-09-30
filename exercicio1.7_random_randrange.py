"""Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa.
O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária 
o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente."""

from random import randrange

nome = input("Escreva o nome do usuário: ")
token = randrange(1000, 9998, 2) # usando o range inicial e final e o numeru 2, ele vai pular de 2 em 2, consequentemente sendo par

""" while token % 2 != 0:
    token = randrange(1000, 9998) """

print(f"o nomé é {nome} e o token é o {token}")
