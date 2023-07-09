"""Interactive Helping System in Python"""
from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[1;29;41m',  # 1 - vermelho
     '\033[1;29;42m',  # 2 - verde
     '\033[1;29;43m',  # 3 - amarelo
     '\033[1;29;44m',  # 4 - azul
     '\033[1;29;45m',  # 5 - roxo
     '\033[7;40m'      # 6 - branco
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)