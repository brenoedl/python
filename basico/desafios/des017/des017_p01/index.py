import moeda
p = float(input('dDigite um preço: R$'))
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'Aumento de 10% é R${moeda.aumentar(p=p, t=10)}')
print(f'Redução de 10% é R${moeda.diminuir(p=p, t=10)}')
