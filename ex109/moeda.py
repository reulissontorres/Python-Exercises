def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)


def moeda(preco, tipo='R$'):
    return f'{tipo}{preco:.2f}'.replace('.', ',')
