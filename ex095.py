"""Aprimorando os Dicionários"""
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for p in range(0, tot):
        partidas.append(int(input(f' - Quantos gols na partida {p+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print('')
while True:
    print('-' * 40)
    opc = int(input('Mostrar dados de qual jogador (999 interrompe): '))
    if opc == 999:
        break
    elif opc >= len(time):
        print(f'ERRO! Não existe jogador com o código {opc}.')
    else:
        print(f' -- LEVANTEMENTO DO JOGADOR {time[opc]["nome"]}')
        for i, v in enumerate(time[opc]["gols"]):
            print(f'    No jogo {i + 1} fez {v} gols.')
print('-' * 40)
print('<< VOLTE SEMPRE >>')
