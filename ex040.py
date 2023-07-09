"""Aquele Clássico da Média"""
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2
print('Tirando {:.1f} e {:.1f} a média é {:.1f}'.format(n1, n2, m))
if m < 5:
    print('\033[1;31mO aluno está REPROVADO!\033[m')
elif 5 <= m < 7:
    print('\033[1;33mO aluno está de RECUPERAÇÃO!\033[m')
elif m >= 7:
    print('\033[1;32mO aluno está APROVADO!\033[m')
