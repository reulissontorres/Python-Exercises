"""Função para Fatorial"""
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um Número
    :param n: O número a ser calculado.
    :param show: Mostrar ou não a conta (opcional).
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    if show:
        for c in range(n, 0, -1):
            print(f'{c}', end=' x 'if c > 1 else ' = ')
    for c in range(n, 0, -1):
        f *= c
    return f


print('-' * 30)
num = 5
print(fatorial(num, show=True))
help(fatorial)
