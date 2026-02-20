from random import randint
from time import sleep
computador = randint(0 , 5)
print('<=>' * 20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
print('<=>' * 20)
jogador = int(input('Em que número eu pencei? '))
print('PROCESSANDO...')
sleep(5)
if computador == jogador:
    print('PARABENS! Você conssequiu me vencer!')
else:
    print('VOCÊ PERDEU! Eu pensei no número {} e não no {}'.format(computador , jogador))
