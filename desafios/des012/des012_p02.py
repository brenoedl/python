nums = []
while True:
    n = int(input('Digite um valor: '))
    if n not in nums:
        nums.append(n)
        print('Número adisionado com sucesso...')
    else:
        print('Número duplicado! Não vou adisionar...')
    res = str(input('Quer conttinuar?  [S/N]: ')).upper().split()[0]
    if res in 'N':
        break
nums.sort()
print(f'Você digitou os valores {nums}.')
