somaidade = 0
mediaidade = 0
nomehvelho = ''
totmulher = 0
maioridadeh = 0
for p in range(1, 5):
    print('----- {}ª pessoa -----'.format(p))
    nome = str(input('nNme: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomehvelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomehvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velhho tem {} anos e se chama {}'.format(maioridadeh, nomehvelho))
print('Ao todo temos {} mulheres com menos de 20 anos'.format(totmulher))
