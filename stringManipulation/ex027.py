"""Primeiro e Último Nome de uma Pessoa"""
n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu último nome é {nome[len(nome)-1]}.')
