"""Jogo da Advinhação v2.0"""
from random import randint
c = randint(0, 10)
print('''Sou seu computador... acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?''')
acertou = False
palpites = 0
while not acertou:
    n = int(input('Qual é o seu palpite? '))
    palpites += 1
    if n == c:
        acertou = True
    else:
        if n < c:
            print('Mais... Tente mais uma vez: ')
        elif n > c:
            print('Menos... Tente mais uma vez: ')
print('Você acertou na {}ª tentativa!'.format(palpites))
#print('Computador: {}\nJogador: {}'.format(c, n))
