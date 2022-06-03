from glob import escape


r = 1
par = inpar = 0
while r != 0:
    r = int(input('Digite um valor: '))
    if  r % 2 == 0:
        par += 1
    else:
        inpar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, inpar))
