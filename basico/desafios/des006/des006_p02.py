Km = float(input('Qual a velocidade atual do carro? '))
if Km > 80:
    print('MULTADO! Você excedeu o limite permitid que é 80Km/h')
    multa = (Km - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')
