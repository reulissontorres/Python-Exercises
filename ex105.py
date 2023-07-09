"""Analisando e Gerando Dicionários"""
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor adicional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações  sobre a situação da turma.
    """
    turma = dict()
    mai = men = 0
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n) / len(n)
    if sit:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['média'] < 5:
            turma['situação'] = 'RUIM'
        else:
            turma['situação'] = 'RAZOÁVEL'
    return turma


resp = notas(4.5, 9, 7.5, 9.5, sit=True)
print(resp)
print('-'*40)
help(notas)
