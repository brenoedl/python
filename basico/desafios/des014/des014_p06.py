time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas parttidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N')
    if resp == 'N':
        break
print('-=' *30)
print(f'{"cod":<5}', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-'*50)
for k, j in enumerate(time):
    print(f'{k:<5}', end='')
    for d in j.values():
        print(f'{str(d):<20}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe o jogador com codigo {busca}.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for p, g in enumerate(time[busca]['gols']):
            print(f'Na partida {p+1} ele fez {g} gols.')
    print('-'*50)
print('<< VOLTE SEMPRE >>')
