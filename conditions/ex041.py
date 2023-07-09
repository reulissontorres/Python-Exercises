"""Classificando Atletas"""
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: \033[31mMIRIM\033[m')
elif idade <= 14:
    print('Categoria: \033[32mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[33mJÚNIOR\033[m')
elif idade <= 20:
    print('Categoria: \033[34mSÊNIOR\033[m')
else:
    print('Categoria: \033[35mMASTER\033[m')
