def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" não é um preço válido.\033[m')
        else:
            #valido = True
            return float(entrada)


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
