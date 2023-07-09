"""Catetos e Hipotenusa"""
from math import hypot
co = float(input('Cateto oposto = '))
ca = float(input('Cateto adjacente = '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
