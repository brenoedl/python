preço = float(input('Qual é o  preço do produlto? R$'))
preçon = preço - preço * 5 / 100
print('O produlto que custava R${:.2f}, na promoção com o desconto de 5% vai custar R${:.2f}.'.format(preço,preçon))
