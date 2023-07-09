"""Detector de Palíndromo"""
frase = str(input('Qual é a frase? ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1] # Usando o fatiamento
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase NÃO É UM PALÍNDROMO')