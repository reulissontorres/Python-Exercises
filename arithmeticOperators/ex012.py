"""Calculando Descontos"""
p = float(input('Preço do produto: R$'))
d = p - (p * 5 / 100)
print('O preço do produto com 5% de desconto é R${:.2f}'.format(d))
