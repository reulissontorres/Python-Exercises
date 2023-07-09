def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação
    :param preco: o preço que se quer reajustar.
    :param taxa: porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def moeda(preco, tipo='R$'):
    return f'{tipo}{preco:.2f}'.replace('.', ',')


def resumo(p=0, aum=10, des=5):
    print('-'*30+f'\n{"RESUMO DO VALOR":^30}\n'+'-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aum}% de aumento: \t{aumentar(p, aum, True)}')
    print(f'{des}% de redução: \t{diminuir(p, des, True)}')
    print('-'*30)
