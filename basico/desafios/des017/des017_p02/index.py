import moeda
p = float(input('dDigite um preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumento de 10% é {moeda.moeda(moeda.aumentar(p=p, t=10))}')
print(f'Redução de 10% é {moeda.moeda(moeda.diminuir(p=p, t=10))}')
