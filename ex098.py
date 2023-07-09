"""Função de Contador"""
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    cont = i
    if i < f:
        while cont <= f:
            print(cont, end=' ')
            cont += p
            sleep(0.3)
    else:
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.3)
    print('FIM!')
    print('-=' * 20)


# Programa principal
print('-=' * 20)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
print('-=' * 20)
contador(ini, fim, pas)
