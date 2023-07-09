"""Cálculo do Fatorial"""
# from math import factorial
n = int(input('Informe um número para calcular seu FATORIAL: '))
c = n
f = 1
# f = factorial(n)
print(f'Calculando {n}! =', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f'{f}')
