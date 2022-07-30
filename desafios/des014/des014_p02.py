from time import sleep
from random import randint
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),'Jogador 2': randint(1, 6),
'Jogador 3': randint(1, 6),'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sortiados')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('== RANKING DOS JOGADORES ==')
for i, c in enumerate(ranking):
    print(f'{i+1}º Lugar {c[0]} com {c[1]}.')
    sleep(1)
