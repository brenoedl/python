def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: paso da contagem
    :return: sem retorno
    """
    cont = i
    while cont <= f:
        print(f'{cont} ' , end='')
        cont += p
    print('FIM!')


def somar(a=0, b=0, c=0):
    """
    -> Soma tres números e mostra na tela
    :param a: primeiro número
    :param b: segundo número
    :param c: treceiro número
    :return: retorna a soma
    """
    s = a + b + c
    print(s)
    return s


help(contador)
print(contador.__doc__)
