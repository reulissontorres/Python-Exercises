"""Aprovando Empréstimo"""
casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financioamento? '))
prest = casa/(anos*12)
min = sal * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de {:.2f}'.format(prest))
if prest <= min:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo NEGADO!')
