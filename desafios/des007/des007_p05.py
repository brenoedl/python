nota1 = float(input('Primeira notta: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('A média entre {:.1f} e {:.1f} é igual {:.1f}.'.format(nota1, nota2, media))
if media < 5:
    print('O aluno está REPROVADO')
elif 7 > media >= 5:
    print('O aluno está em RECULPERAÇÃO')
elif media >= 7:
    print('O aluno está APROVADO')
