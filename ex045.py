"""GAME: Pedra, Papel e Tesoura"""
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('\033[36m-='*3, 'JOKENPO!!!', '-='*3)
print('''\033[mSuas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
while True:
    jogador = int(input('Escolha sua jogada: '))
    if jogador == 0 or jogador == 1 or jogador == 2:
        break
    print('Jogada inválida! ', end='')
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-='*11)
print('Jogador jogou: {}'.format(itens[jogador]))
print('Computador jogou: {}'.format(itens[comp]))
print('-='*11)
if comp == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
elif comp == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
elif comp == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
