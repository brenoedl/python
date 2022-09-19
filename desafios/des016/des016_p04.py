def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número intero valido.\033[m')
        if ok == True:
            break
    return valor


n = leiaint('Digite um númeroo: ')
print(f'Você acabou de digitar o número {n}.')
