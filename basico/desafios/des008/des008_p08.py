frase = str(print('Digite uma frase: ')).strip().upper()
palavas = frase.split()
jonto = ''.join(palavas)
inverso = ''
for letras in range(len(jonto)-1, -1, -1):
    inverso += jonto[letras]
print('O inverso de {} é {}'.format(jonto, inverso))
if inverso == jonto:
    print('Temos um PALINDROMO')
else:
    print('Está frase não é um PALINDROMO')
