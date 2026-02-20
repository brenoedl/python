tot = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    tot += 1
    soma += num
print(f'Você digitou {tot} números e a soma é {soma}.')
