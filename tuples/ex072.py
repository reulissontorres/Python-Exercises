"""Número por Extenso"""
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {extenso[n]}.')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print('Tente novamente. ', end='')
print('FIM DO PROGRAMA')