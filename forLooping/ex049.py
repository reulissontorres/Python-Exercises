"""Tabuada v2.0"""
n = int(input('\033[1;35mEscolha um número inteiro:\033[1;31m '))
for c in range(1, 10+1):
    print(f'{n} x {c:2} = {n * c}')
