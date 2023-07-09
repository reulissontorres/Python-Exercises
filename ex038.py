"""Comparando Números"""
n1 = int(input('\033[1;33mPrimeiro\033[m valor: '))
n2 = int(input('\033[1;35mSegundo\033[m valor: '))
if n1 > n2:
    print('O \033[1;33mPRIMEIRO\033[m valor é maior.')
elif n2 > n1:
    print('O \033[1;35mSEGUNDO\033[m valor é maior.')
else:
    print('Os dois são \033[1;36mIGUAIS\033[m.')
