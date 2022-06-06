from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
[ 2 ] mutipliar
[ 3 ] qual é o maior
[ 4 ] novos valores
[ 5 ] sair do programa''')
    opção = int(input('qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produlto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produlto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior entre {n1} e {n2} é {maior}')
    elif opção == 4:
        print('Iforme os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invvalida...Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do prograama volte sempre')
