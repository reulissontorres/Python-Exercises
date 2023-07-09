"""Validação de Dados"""
s = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Dados inválidos. Qual é o seu sexo? [M/F] ')).strip().upper()[0]
if s == 'M':
    print('Sexo masculino registrado com sucesso.')
elif s == 'F':
    print('Sexo feminino registrado com sucesso.')
