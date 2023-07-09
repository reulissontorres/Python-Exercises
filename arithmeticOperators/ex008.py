"""Conversor de Medidas"""
med = float(input('Distância em metros: '))
km = med / 1000
hm = med / 100
dam = med / 10
dm = med * 10
cm = med * 100
mm = med * 1000
print('Em Quilômetros: {}'.format(km))
print('Em Hectômetros: {}'.format(hm))
print('Em Decâmentros: {}'.format(dam))
print('Em Decímetros: {:.0f}'.format(dm))
print('Em Centímetros: {:.0f} '.format(cm))
print('Em Milímetros: {:.0f}'.format(mm))
