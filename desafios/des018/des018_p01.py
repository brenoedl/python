def leiaint(msg):
    while True:
        try:
            n = str(input(msg))
            n = int(n)
        except:
            print('\033[31mERRO! Digite um número inteuro valido\033[m')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = str(input(msg))
            n = float(n)
        except:
            print('\033[31mERRO! Digite um número real valido\033[m')
        else:
            return n


i = leiaint('Digite um número inteuro: ')
r = leiafloat('Digite um número real: ')
print(f'O número inteuro foi {i} e o real foi {r}.')
