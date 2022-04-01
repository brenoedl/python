Dia = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
pagar = Dia * 60 + Km * 0.15
print('O total a ser pago é de R${:.2f}'.format(pagar))
