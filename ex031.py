"""Custo da Viagem"""
d = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
p = d * 0.50 if d <= 200 else d * 0.45
print('O preço da viagem é de R${:.2f}.'.format(p))
