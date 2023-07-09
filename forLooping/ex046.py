"""Contagem Regressiva"""
from time import sleep
for c in range(10, -1, -1):
    print('\033[1;34m', c)
    sleep(1)
print('\033[1;34m FELIZ ANO NOVO!!!\033[m')
