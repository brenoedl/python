grupo = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
            resp = str(input('Quar continuar? [S/N]')).strip().upper()[0]
            if resp in 'SN':
                break
            print('ERRO! Por favor digite apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(grupo)} pessoas cadastradas.')
media = soma / len(grupo)
print(f'A media de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão assima da mediaa:')
for p in grupo:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<<< ENCERRADO >>>')
