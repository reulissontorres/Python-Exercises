"""Análise de Dados em uma Tupla"""
numeros = (int(input('Digite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite o último valor: ')))
print(f'Você digitou os valores {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primero valor 3 está na {numeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares são ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
