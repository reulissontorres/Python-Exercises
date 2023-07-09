"""Analisador Completo"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
mul20 = 0
nomevelho = ''
for c in range(1, 5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if (c == 1) and (sexo in 'Mm'):
        maioridadehomem = idade
        nomevelho = nome
    if (idade > maioridadehomem) and (sexo in 'Mm'):
        maioridadehomem = idade
        nomevelho = nome
    if (idade < 20) and (sexo in 'Ff'):
        mul20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {} anos.'.format(mediaidade))
print('O nome do homem mais velho é {} com {} anos.'.format(nomevelho, maioridadehomem))
print('O total de mulheres com menos de 20 anos é {}.'.format(mul20))
