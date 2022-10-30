from time import sleep
from lib.interfase import *
from lib.arquivo import *

arq = 'breno_curso_em_video.txt'
if not arqexiste(arq):
    criaraqr(arq)

cabesalio('cadastro de pessoas')
while True:
    resp = menu(['Ver todas as pessoas', 'Catastrar uma nova pessoa', 'Sair do sistema'])
    if resp == 1:
        lerarq(arq)
    elif resp == 2:
        cabesalio('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabesalio('saindo do sistema... até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção validda\033[m')
    sleep(2.5)
