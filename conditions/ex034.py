"""Aumentos Múltiplos"""
s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250.00:
    novo = s + (s * 0.10)
else:
    novo = s + (s * 0.15)
print('Quem ganhava {:.2f} passa a ganhar R${:.2f} agora.'.format(s, novo))
