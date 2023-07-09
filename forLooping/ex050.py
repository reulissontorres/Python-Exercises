"""Soma dos Pares Ímpares"""
spar = simpar = 0
contpar = contimpar = 0
for c in range(1, 7):
    n = int(input(f'Informe o {c}° valor inteiro: '))
    if n % 2 == 0:
        spar += n
        contpar += 1
    else:
        simpar += n
        contimpar += 1
print('A soma dos {} números pares é {}'.format(contpar, spar))
print('A soma dos {} números ímpares é {}'.format(contpar, simpar))
