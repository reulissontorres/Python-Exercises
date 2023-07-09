"""Super Progressão Aritmética v3.0"""
print('Gerador de P.A.')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{an}', end=' ⇨ ')
        an += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
