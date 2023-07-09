"""Função que Calcula Área"""
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.1f}m².')


print('Controle de Terrenos')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
