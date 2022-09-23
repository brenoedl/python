def notas(*n, sit=False):
    """-> Função para analisar notas e situações de varios alunos.
:param n: uma ou mais notas dos alunos (aceita varias)
:param sit: (opcional) indicando se deve ou não adicionar a situação
:return: dicionário com variaas imformações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(10, 3.6, 5.2, 4.3, sit=True)
print(resp)
help(notas)
