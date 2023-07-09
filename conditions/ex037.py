"""Conversor de Bases Numéricas"""
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é {}.'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}.'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para EXADECIMAL é {}.'.format(n, hex(n)[2:]).upper())
else:
    print('Escolha invárlida. Tente novamente.')
