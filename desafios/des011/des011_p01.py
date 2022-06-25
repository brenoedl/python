nums = ('zero', 'um', 'dois', 'tres', 'quatro', 'sinco',
'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    pos =int(input('Digite um múmero entre 0 a 20: '))
    if 0 <= pos <= 20:
        break
    print('Tente novamente.' ,end=' ')
print(f'Você digitou o número {nums[pos]}.')
