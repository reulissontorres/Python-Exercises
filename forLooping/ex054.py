"""Grupo da Maioridade"""
from datetime import date
ano = date.today().year
mai: int = 0
men: int = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano nasceu a {c}ª pessoa? '))
    idade = ano - nasc
    if idade >= 21:
        mai += 1
    else:
        men += 1
print(f'Ao todo tivemos {mai} pessoas maiores de idade.')
print(f'também tivemos {men} pessoas menores de idade.')
