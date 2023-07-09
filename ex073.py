"""Tplas com Times de Futebol"""
times = ('Palmeiras', 'Cotinthians', 'Fluminense', 'Atlético-MG', 'Atlético-PR',
         'Flamengo', 'Internacional', 'Bragantino', 'Santos', 'São Paulo',
         'Botafogo', 'Ceará', 'Goiás', 'América-MG', 'Avaí',
         'Cuiabá', 'Coritba', 'Atlético-GO', 'Juventude', 'Fortaleza')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os  5 primeiros colocados são: {times[:5]}')
print('-='*15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print('O São Paulo está na {}ª colocação.'.format(times.index('São Paulo')+1))
