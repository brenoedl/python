from time import sleep
from lib.interfase import *

cabesalio('cadastro de pessoas')
while True:
    resp = menu(['Ver todas as pessoas', 'Catastrar uma nova pessoa', 'Sair do sistema'])
    if resp == 1:
        cabesalio('opc 01')
    elif resp == 2:
        cabesalio('opc 02')
    elif resp == 3:
        cabesalio('saindo do sistema... até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção validda\033[m')
    sleep(2.5)
