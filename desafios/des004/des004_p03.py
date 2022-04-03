from math import radians, sin, cos, tan
angulo = float(input('Digite um ángulo que você queser:'))
seno = sin(radians(angulo))
print('O ángulo de {} tem o seno de {:.2f}.'.format(angulo, seno))
coseno = cos(radians(angulo))
print('O ángulo de {} tem o coseno de {:.2f}.'.format(angulo, coseno))
tangente = tan(radians(angulo))
print('O ángulo de {} tem a tangente de {:.2f}.'.format(angulo, tangente))
