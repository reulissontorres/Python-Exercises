"""Valores Únicos em uma Lista"""
valores = list()
while True:
    resp = ' '
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar...')
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
valores.sort()
print(f'O valores digitados foram {valores}')
