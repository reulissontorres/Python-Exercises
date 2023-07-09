"""Quebrando um Número"""
from math import trunc
n = float(input('Digite um valor: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(n, trunc(n)))
