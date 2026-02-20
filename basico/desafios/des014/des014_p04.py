jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas parttidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'No canpo {k} tem o valor {v}.')
print('-='*30)
print(f'O jpgador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for p, g in enumerate(jogador['gols']):
    print(f'Na partida {p+1}ª fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
