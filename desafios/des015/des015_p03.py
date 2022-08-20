from time import sleep

def contador(i, f, p):
    print('-' * 30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(3)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont += p 
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont -= p
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 30)
print('Agora é sua vez de personalizar a conntagem!')
inicio = int(input('inicio: '))
fim = int(input('fim: '))
paso = int(input('paso: '))
contador(inicio, fim, paso)
