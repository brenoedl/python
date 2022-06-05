sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido Por favor informe o seu sexo: [M/F] ')).strip().upper()[0]
print(f'O sexo {sexo} foi cadrastrado com sucesso.')
