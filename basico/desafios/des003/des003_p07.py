lar = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
aria = lar*alt
print('Sua parede tem {}x{} metros e árie é de {}m²'.format(lar,alt,aria))
tinta = aria/2
print('Para pintar essa parede você vai precisar {}litros de tinta'.format(tinta))
