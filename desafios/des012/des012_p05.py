nums = list()
numspar = list()
numsimpar = list()
while True:
    nums.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for s, v in enumerate(nums):
    if v % 2 == 0:
        numspar.append(v)
    else:
        numsimpar.append(v)
print(f'A lista completa é {nums}.')
print(f'A lista de peres é {numspar}.')
print(f'A lista de impares é {numsimpar}.')
