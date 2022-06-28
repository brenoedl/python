listagem = ('Lapis', 2.69,
'Borracha', 1,
'Caderno', 20.8,
'Estojo', 14.99,
'Transferidor', 6.78,
'Mochila', 124.89,
'Canetas', 25.63,
'Livro', 60,
'Compasso', 24)
print('-'*40)
print(f'{"LISTAGEM DE PRODULTO":^40}')
print('-'*40)
for pos in range(0 , len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-'*40)
