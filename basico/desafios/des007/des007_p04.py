from datetime import date
atual = date.today().year
nnsc = int(input('Ano de nascimento: '))
idade = atual - nnsc
print('Quem nasceu em {} tem {} anos em {}.'.format(nnsc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos.'.format(saldo))
    ano  = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
