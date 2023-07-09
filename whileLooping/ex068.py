"""Jogo do Par ou Ímpar"""
import random
soma = tot = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    comp = random.randint(1, 10)
    num = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = comp + num
    print(f'Você jogou {num} e o computador {comp}. Total de {soma}', end=' ')
    print(f'DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if pi == 'P':
        if soma % 2 == 'P':
            print('Você VENCEU!')
            tot += 1
        else:
            print('Você PERDEU!')
            break
    elif pi == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            tot += 1
        else:
            print('Você PERDEU!')
            break
        print('--' * 15)
        print('Vamos jogar novamente...')

print('=-'*15)
if tot == 0:
    print('GAME OVER! Você não acertou nenhuma vez.')
elif tot == 1:
    print('GAME OVER! Você venceu só 1 vez.')
else:
    print(f'GAME OVER! Você venceu {tot} vezes consecutivas.')