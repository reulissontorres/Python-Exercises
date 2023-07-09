"""Validando Entrada de Dados em Python"""
def leiaInt(msg):
    print('-' * 30)
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.strip().isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
