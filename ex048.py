"""Soma Ímpares Múltiplos de Três"""
soma = cont = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de dos {} números ímpares e múltiplos de 3 é {}'.format(cont, soma))
