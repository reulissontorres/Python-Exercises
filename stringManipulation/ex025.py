"""Procurando uma String Dentro da Outra"""
nome = str(input('Digite seu nome: ')).lower().split()
print(f'Seu nome tem Silva? {"silva" in nome}')
