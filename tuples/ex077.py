"""Contando Vogais em Tupla"""
palavras = ('alisson', 'lillia', 'reulisson', 'gabriel', 'karina', 'layla', 'torres',
            'silva', 'lailio', 'eike', 'joaquim', 'rosário', 'lucimar',)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aáãâeéêiíoóõôu':
            print(letra, end=' ')
