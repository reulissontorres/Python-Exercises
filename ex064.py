"""Tratando Vários Valores v1.0"""
c = tot = som = 0
print('O programa só para quando você digita "999".')
while c != 999:
    c = int(input('Digite um número: '))
    if c != 999:
        tot += 1
        som += c
print('O total de números digitados foi {} .'.format(tot))
print('A soma entre eles é {}.'.format(som))
