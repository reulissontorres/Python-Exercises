"""Funções para Votação"""
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'VOTO NEGADO.'
    elif idade < 18 or idade > 70:
        return 'VOTO OPCIONAL.'
    else:
        return 'VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
