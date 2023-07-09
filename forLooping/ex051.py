"""Progressão Aritmética"""
a1 = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
an = 0
print('Os 10 primeiros termos dessa são P.A.:')
for c in range(1, 10+1):
    an = a1 + (c - 1) * r
    print(an, end=' ⇨ ')
print('ACABOU')
