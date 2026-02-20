from random import randint
from time import sleep
def sorteia(lista):
    print('Os valores sorteados foram ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(1)
    print()


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somamdo os valores pares de {lista} temos {soma} ')


numeros = list()
sorteia(numeros)
somapar(numeros)
