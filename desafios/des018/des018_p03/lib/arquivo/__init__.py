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
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao abrir o aarquivo.')
    else:
        cabesalio('pessoas cadastradas')
        for lin in a:
            dado = lin.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            print(linha())
    finally:
        a.close()


def cadastrar(narq, nome='desconhecido', idade=0):
    try:
        a = open(narq, 'at')
    except:
        print('Houve um erro na abertora do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro no cadastro.')
        else:
            print(f'Novo cadastro de {nome} adiccionadoo')
        finally:
            a.close()
