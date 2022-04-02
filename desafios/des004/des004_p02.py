from math import hypot
co = float(input('Coprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = hypot(co , ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
