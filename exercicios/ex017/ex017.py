teste = list()
teste.append('Breno')
teste.append(20)
galera = list()
galera.append(teste[:])
teste[0] = 'Elis'
teste[1] = 3
galera.append(teste[:])
teste[0] = 'Renan'
teste[1] = 1
galera.append(teste[:])
print(galera)
print(galera[0][0])
print(galera[1][1])
print(galera[2][0])
