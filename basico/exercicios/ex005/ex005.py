n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1+n2
sb = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
rd = n1%n2
e = n1**n2
print('A soma é {} e a sobtração é {}'.format(s,sb),end=' ')
print('O produto é {} e a divisão é {:.3f}'.format(m,d),end=' ')
print('A divisão inteira é {} e oresto da divisão é {}'.format(di,rd),end=' ')
print('A exponenciação é {}'.format(e))
