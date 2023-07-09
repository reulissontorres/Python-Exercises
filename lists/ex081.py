"""Extraindo Dados de uma Lista"""
numeros = []
while True:
    resp = ' '
    numeros.append(int(input('Digite um número: ')))
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('Resposta inválida. Tente de novo.')
    if resp == 'N':
        break
print('-='*30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
print('O valor 5 foi econtrado na lista.') if 5 in numeros else print('O valor 5 NÃO foi encontrado na lista.')
