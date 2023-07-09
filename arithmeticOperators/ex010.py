"""Conversor de Moedas"""
real = float(input('Quanto dineiro você tem na carteira? R$'))
dolar = real / 5.41
euro = real / 5.46
iene = real / 0.039
print('Com R${:.2f} você pode comprar: \nUS${:.2f} \n€{:.2f} \n¥{:.2f}'.format(real, dolar, euro, iene))
