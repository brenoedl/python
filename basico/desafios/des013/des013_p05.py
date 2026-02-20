from random import randint
from time import sleep
jogo = list()
jogos = list()
totj = 0
print('-' * 30)
print(f'{"Jogue na méga sena":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while totj <= quant-1:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    totj += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' *3)
for i , j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
