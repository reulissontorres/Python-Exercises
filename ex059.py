"""Criando um Menu de Opções"""
from time import sleep
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
n = 0
print(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos valores\n [5] Sair')
while n != 5:
    print('-=' * 15)
    n = int(input('=> O que você deseja fazer? '))
    if n == 1:
        print('A soma entre {} e {} é {}.'.format(v1, v2, v1+v2))
    elif n == 2:
        print('O produto entre {} e {} é {}.'.format(v1, v2, v1*v2))
    elif n == 3:
        if v1 > v2:
            print('O maior valor é {}.'.format(v1))
        elif v2 > v1:
            print('O maior valor é {}.'.format(v2))
        else:
            print('Os dois valores são iguais.')
    elif n == 4:
        v1 = float(input('Digite um valor: '))
        v2 = float(input('Digite outro valor: '))
    elif n == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Escolha inválida!')
print('Fim do Programa! Volte Sempre!')