nums = []
while True:
    nums.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
nums.sort(reverse=True)
print(f'Você digitou {len(nums)} elementos.')
print(f'Os valores em ordem decrescente são {nums}.')
if 5 in nums:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
