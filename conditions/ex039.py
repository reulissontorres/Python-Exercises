"""Alistamento Militar"""
from datetime import date
atual = date.today().year
sexo = str(input('Seu sexo [M/F]: ')).strip().upper()
if sexo == 'F':
    print('Você não precisa fazer alistamento militar obrigatório!')
elif sexo == 'M':
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar  IMEDIATAMENTE!')
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        if saldo == 1:
            print('Você já deveria ter se alistado há 1 ano.')
        else:
            print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}'.format(ano))
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        if saldo == 1:
            print('Falta apenas 1 ano para o alistamento.')
        else:
            print('Ainda faltam {} anos para o alistamento.'.format(saldo))
else:
    print('Opção inválida. Tente novamente.')