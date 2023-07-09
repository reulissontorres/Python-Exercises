"""Maior e Menores Valores"""
resp = 'S'
media = soma = quant = maior = menor = 0
while resp not in 'Nn':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = num
        menor = num
    elif quant > maior:
        maior = quant
    elif quant < menor:
        menor = quant
    resp = str(input('Você quer contimuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media:.1f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
