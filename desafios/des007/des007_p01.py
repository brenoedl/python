casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimmo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos) , end=' ')
print('a prestação é de R${:.2f}.'.format(prestação))
print('Você recebi  R${:.2f} por tanto'.format(salario) , end=' ')
if prestação <= minimmo:
    print('Empréstimo podee ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
