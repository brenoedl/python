sal = float(input('Qual o salario do funcionário? R$'))
saln = sal + sal * 15 / 100
print('Um funcionário que ganhava R${:.2f}, com 15%5 de aummento, passa a receber R${:.2f}.'.format(sal,saln))
