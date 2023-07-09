"""Dobro, Triplo, Raiz Quadrada"""
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = pow(n, (1/2))
print('O dobro de {} é {} \nO triplo é {} \nE a raiz quadrada é {:.2f}'.format(n, d, t, r))
