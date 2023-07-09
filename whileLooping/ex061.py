"""Progressão Aritmética v2.0"""
print('Gerador de P.A.')
print('-=' * 10)
a1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
an = a1
c = 0
while c < 10:
    print(an, end=' ⇨ ')
    an += r
    c += 1
print('FIM')
