"""Jogo da Advinhação v1.0"""
from random import randint
from time import sleep
comp = randint(1, 6) #Computador escolhe um número
print('-=-'*20)
print('Vou pensar num número entre 1 e 6. Tente Advinhar...')
print('-=-'*20)
player = int(input('Em que número eu pensei? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(1.5)
if comp == player:
    print('PARABÉNS! Você conseuiu me vencer!')
else:
    print('EU GANHEI! Eu pensei no número {} e não no {}!'.format(comp, player))
