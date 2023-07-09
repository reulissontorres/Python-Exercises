"""Radar Eletrônico"""
print('O LIMITE DE VELOCIDADE É 80KM/H')
v = float(input('Velocidade atual do veículo: '))
if v > 80.0:
    m = (v - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
else:
    print('Velocidade permitida!')
print('Tenha um bom dia! Dirija com segurança!')
