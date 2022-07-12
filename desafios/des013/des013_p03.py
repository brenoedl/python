matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for ml in range(0, 3):
    for mc in range(0, 3):
        matriz[ml][mc] = int(input(f'Digite um valor para [{ml}, {mc}]: '))
print('-=' *20)
for ml in range(0, 3):
    for mc in range(0, 3):
        print(f'[ {matriz[ml][mc]} ]', end='')
    print()
