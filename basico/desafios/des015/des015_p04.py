from time import sleep
def comparador(*num):
    cont = maior = 0
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0 or valor > maior:
            maior = valor
        cont += 1
        sleep(1)
    print(f'Foram informados {cont} valores e o maior valor foi {maior}.')


comparador(3, 5, 2, 9)
comparador(1, 5, 7, 4, 6)
comparador(1, 2)
comparador(4, 7, 0)
comparador(6)
comparador()
