def notas(lista, sit=False):
    """=> Função para analisar notas e situações de vários alunos.
    param: lista = uma ou mais notas de aluno(s)
    param: sit (valor opcional) = indica a situação do aluno ou turma
    return = dicionario com varias informações do aluno/turma"""
    info = dict()
    maior = menor = media = 0
    for i in range(len(lista)):
        if i == 0:
            maior = menor = lista[0]
        elif lista[i]>maior:
            maior = lista[i]
        elif lista[i]<menor:
            menor = lista[i]
        media += lista[i]
    media = media/len(lista)
    info['maior'] = maior
    info['menor'] = menor
    info['media'] = media
    info['quantidade'] = len(lista)
    if sit:
        if media > 8:
            sit = 'BOM'
        elif media >= 6:
            sit = 'RAZOAVEL'
        elif media < 6:
            sit = 'RUIM'
        info['situacao'] = sit
    return info


vetor = [2.0, 4.6, 6.2, 7.8, 9.1, 10]
print(notas(vetor, sit=True))
help(notas)