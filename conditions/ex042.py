"""Analisando Triângulos v2.0"""
A = float(input('Lado A do triângulo: '))
B = float(input('Lado B do triângulo: '))
C = float(input('Lado C do triângulo: '))
if (A < B + C) and (B < A + C) and (C < A + B):
    print('\033[32mOs segmentos acima PODEM FORMAR um triângulo ', end='')
    if A != B != C != A:
        print('ESCALENO\033[m')
    elif A == B == C:
        print('EQUILÁTERO\033[m')
    else:
        print('ISÓCELES\033[m')
else:
    print('\033[31mOs segmentos acima NÃO PODEM FORMAR um triângulo.\033[m')