import moeda
p = float(input('dDigite um preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Aumento de 10% é {moeda.aumentar(p, 10, True)}')
print(f'Redução de 10% é {moeda.diminuir(p, 10, True)}')
