def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita váris)
    :param sit: valor opconal, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    ficha = dict()
    ficha['total'] = len(n)
    ficha['maior'] = max(n)
    ficha['menor'] = min(n)
    ficha['média'] = sum(n) / len(n)
    if sit:
        if ficha['média'] >= 7:
            ficha['sit'] = 'BOA'
        elif ficha['média'] >= 5:
            ficha['sit'] = 'RAZOÁVEL'
        else:
            ficha['sit'] = 'RUIM'
    return ficha


resp = notas(5.5, 2.5, 1.5)
print(resp)
help(notas)
