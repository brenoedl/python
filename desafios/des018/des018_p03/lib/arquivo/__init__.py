from lib.interfase import *

def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaraqr(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao abrir o aarquivo')
    else:
        cabesalio('pessoas cadastradas')
        print(a.read())
