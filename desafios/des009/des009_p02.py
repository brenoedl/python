from random import randint
computador = randint(0, 10)
print('''Sou seu computador... Acabei de pençar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual o seu paupiti? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
print(f'Acertou com {tentativas} paupiites')
