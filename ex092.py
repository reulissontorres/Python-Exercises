"""Cadastro de Trabalador"""
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
dados['Idade'] = ano_atual - nasc
dados['CTPS'] = int(input('Casteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contratação'] + 35) - datetime.now().year
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
