c = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7m')

def ajuda(com):
    titulo(f'Acessando o manul comando \'{com} \'',4)
    print(c[6], end='')
    help(com)
    print(c[0])


def titulo(msg, cor=0):
    t = len(msg) + 4
    print(c[cor], end='')
    print('=' * t)
    print(f'  {msg}')
    print('=' * t)
    print(c[0])


commamdo = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    commamdo =str(input('Função ou Biblioteca > '))
    if commamdo.upper() == 'FIM':
        break
    else:
        ajuda(commamdo)
titulo('VOLTE SENPRE!', 1)
