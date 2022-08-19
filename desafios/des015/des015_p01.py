def aria(larg, comp):
    a = larg * comp
    print(f'A ária de um terreno {larg}x{comp} é de {a}m².')


print('Controle de Terreno')
print('-'*20)
l = float(input('Largura do terreno [m]: '))
c = float(input('Comprimento do terreno [m]: '))
aria(l, c)
