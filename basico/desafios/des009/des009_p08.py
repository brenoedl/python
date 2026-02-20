num = soma = cont = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    cont += 1
print(f'Você digitou {cont - 1} número e a soma foi {soma - 999}')
