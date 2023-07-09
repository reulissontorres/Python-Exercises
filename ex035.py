"""Analisando Triângulo v1.0"""
print('-='*20)
print('Analisador de Triângulos')
r1 = float(input('1° segmento: '))
r2 = float(input('2° segmento: '))
r3 = float(input('3° segmento: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
