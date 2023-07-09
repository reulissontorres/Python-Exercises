"""Dividindo Valores em Várias Listas"""
numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Informe um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('Opção inválida. Tente de novo.')
    if resp == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=' * 30)
print(f'A lista completa é {sorted(numeros)}')
print(f'A lista de pares é {sorted(pares)}')
print(f'A lista de ímpares é {sorted(impares)}')
