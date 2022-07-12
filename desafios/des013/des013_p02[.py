nums = [[], []]
val = 0
for c in range(1, 8):
    val = int(input(f'Digite o {c}° valor: '))
    if val % 2 == 0:
        nums[0].append(val)
    else:
        nums[1].append(val)
print('-='*20)
nums[0].sort()
nums[1].sort()
print(f'Os números pares foram: {nums[0]}')
print(f'Os números impares foram: {nums[1]}')
