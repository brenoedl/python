total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ''
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi {total:.2f}')
print(f'Temos {totmil} produtos com mais de R$ 1000.00')
print(f'O produto mais barato é {barato} e custa R$ {menor:.2f}')
