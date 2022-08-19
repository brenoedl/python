def titulo(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)


def soma(a, b):
    s = a + b
    print(f'A soma entre {a} e {b} é igual {s}.')


def somamqd(*num):
    s = 0
    for valor in num:
        s += valor
    print(f'A soma entre {num} é igual {s}.')


titulo('ccadrastro')
soma(5, 2)
somamqd(6, 2, 5, 8)
