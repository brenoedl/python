matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = stcol = mai = 0 
for ml in range(0, 3):
    for mc in range(0, 3):
        matriz[ml][mc] = int(input(f'Digite um valor para [{ml}, {mc}]: '))
print('-=' *20)
for ml in range(0, 3):
    for mc in range(0, 3):
        print(f'[{matriz[ml][mc]:^5}]', end='')
        if matriz[ml][mc] % 2 == 0:
            spar += matriz[ml][mc]
    print()
print('-=' *20)
print(f'A soma de todos os valores pares é {spar}.')
for l in range(0, 3):
    stcol += matriz[l][2]
print(f'A soma da terceira coluna é {stcol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
