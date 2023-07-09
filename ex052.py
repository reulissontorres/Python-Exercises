"""Números Primos"""
n = int(input('Informe um número inteiro: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end='')
        div += 1
    else:
        print('\033[32m', end='')
    print('{} '.format(c), end='')
print('\033[m\nO número {} foi divisível {} vezes'.format(n, div))
if div == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO.')
