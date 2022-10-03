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
