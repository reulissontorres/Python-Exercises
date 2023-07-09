"""Vários Números com Flag"""
tot = soma = 0
print('Digite 999 para parar')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    tot += 1
    soma += n
print(f'A soma dos {tot} valores foi {soma}!')
