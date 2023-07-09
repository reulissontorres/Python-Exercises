"""Gerenciador de Pagamento"""
print('\033[1;36m{:=^40}\033[m'.format(' LOJAS GUANABARA '))
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros''')
print('\033[1;36m=\033[m'*40)
c = int(input('Qual é a opção? '))
if c == 1:
    total = p - (p * 0.10)
elif c == 2:
    total = p - (p * 0.05)
elif c == 3:
    total = p
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif c == 4:
    total = p + (p * 0.20)
    totparc = int(input('Em quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = p
    print('Opção inválida! Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, total))
