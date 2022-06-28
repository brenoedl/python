times = ('Palmeiras', 'Corinthians', 'Athetico-PR', 'Iternasonal', 'Athetico-MG', 'Fluminnense',
'Botafogo', 'Santos', 'São Paulo', 'Bragantihno', 'Avai',
'Athetico-GO', 'Ceará SC', 'Flamengo', 'América-MG', 'Coritiba',
'Goias', 'Cuiaba', 'Fortaleza', 'Juventude')
print(f'Lista dos times do brasileirão por classificação: {times} ')
print(f'Lista dos times do brasileirão em ortem alfabética: {sorted(times)} ')
print(f'Os 5 primeiros são {times[:5]} ')
print(f'Os 4 ultimos são {times[-4:]} ')
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição')
