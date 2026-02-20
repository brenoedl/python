sal = float(input('Qual o salario de um funcionario? R$'))
if sal <= 1250:
    nsal = sal + sal * 15 / 100
else:
    nsal = sal + sal * 10 / 100
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal , nsal))
