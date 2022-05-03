nome = str(input('Qual é o seu nome? '))
if nome == 'Breno' or nome == 'Cézar' or nome == 'Renan' or nome == 'Roberto':
    print('Que nome de homen bonito')
elif nome == 'Ellen' or nome == 'Elis' or nome == 'Josefa' or nome == 'Daniele':
    print('Que nome de mulher bonito')
else:
    print('Que nome comum')
print('Tenha um bom dia, {}!'.format(nome))
