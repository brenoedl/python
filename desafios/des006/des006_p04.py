distancia = float(input('Qual é a distancia da sua viagen? '))
print('Você está prestes a começar uma viagen de {}Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua viagem é de R${:.2f}'.format(preco))
