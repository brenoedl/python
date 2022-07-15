fichas = list()
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('nota 1: '))
    nota_2 = float(input('nota 2: '))
    media = (nota_1 + nota_2) / 2
    fichas.append([nome, [nota_1, nota_2], media])
    resp = str(input('Quer continoar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for c, a in enumerate(fichas):
    print(f'{c:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('finalizando...')
        break
    if opc <= len(fichas) -1:
        print(f'As notas de {fichas[opc][0]} são {fichas[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
