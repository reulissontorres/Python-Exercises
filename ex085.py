"""Listas com Pares e Ímpares"""
valores = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    elif n % 2 == 1:
        valores[1].append(n)
print('-=' * 20)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares são {valores[0]}')
print(f'Os valores ímpares são {valores[1]}')