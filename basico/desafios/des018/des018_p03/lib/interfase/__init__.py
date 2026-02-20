def leiaint(msg):
    while True:
        try:
            n = str(input(msg))
            n = int(n)
        except:
            print('\033[31mERRO! Digite um número inteuro valido\033[m')
        else:
            return n


def linha(tan=42):
    return '=' * tan


def cabesalio(txt):
    print(linha())
    print(f'{txt:^42}')
    print(linha())


def menu(lista):
    c = 1
    for iten in lista:
        print(f'\033[33m{c}\033[m - \033[34m{iten}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32msua opção:\033[m ')
    return opc
