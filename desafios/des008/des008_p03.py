soma = 0
goran = 0
for yugi in range(1, 501, 2):
    if yugi % 3 == 0:
        soma += yugi
        goran += 1
print('A soma de todos os {} valores solicitados é {}'.format(goran, soma))
