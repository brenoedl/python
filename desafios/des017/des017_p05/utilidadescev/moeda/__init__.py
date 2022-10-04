def aumentar(p=0, t=0, f=False):
    res = p + (p * t / 100)
    return res if not f else moeda(res)


def diminuir(p=0, t=0, f=False):
    res = p - (p * t / 100)
    return res if not f else moeda(res)


def dobro(p=0, f=False):
    res = p * 2
    return res if not f else moeda(res)


def metade(p=0, f=False):
    res = p / 2
    return res if not f else moeda(res)


def moeda(p=0, m='R$'):
    return f'{m}{p:.2f}'.replace('.' , ',')


def resumo(p=0, ta=0, tr=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analizado:  {moeda(p)}')
    print(f'Dobro do preço:   {dobro(p, True)}')
    print(f'Metade do preço:  {metade(p, True)}')
    print(f'{ta}% de aumento: {aumentar(p, ta, True)}')
    print(f'{tr}% de redução: {diminuir(p, tr, True)}')
    print('-' * 30)
