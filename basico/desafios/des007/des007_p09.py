print('{:=^40}'.format('  LOJA DO BRENO  '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    prestação = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(prestação))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    parcela = int(input('Quantas parcelas? '))
    prestação = total / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, prestação))
else:
    total = preço
    print('Opção invalida de pagamento TENTE NOVAMENTE')
print('A sua compra que custava R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
