import random
import time
import operator
jogadores = {}
for j in range(0, 4):
    jogadores[f'Jogador {j+1}'] = random.randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    time.sleep(0.5)
ranking = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)
print('='*30)
print('          ==RANKING==')
contador = 1
for x in range(len(ranking)):
    if x == 0:
        print(f'  {contador}º - {ranking[x][0]} com {ranking[x][1]} pontos.')
    elif ranking[x][1] == ranking[x - 1][1]:
        print(f'       {ranking[x][0]} com {ranking[x][1]} pontos.')
    else:
        contador += 1
        print(f'  {contador}º - {ranking[x][0]} com {ranking[x][1]} pontos.')




resultado = {'jogador1': random.randint(1,6),
             'jogador2': random.randint(1,6),
             'jogador3': random.randint(1,6),
             'jogador4': random.randint(1,6),
             'jogador5': random.randint(1,6),
             'jogador6': random.randint(1,6)}
rank = dict()
print('Valores sorteados:')
for k, v in resultado.items():
    print(f'{k} tirou {v}')
    time.sleep(1)
print('-='*30)
print(' == RANKING DOS JOGADORES == ')
rank = sorted(resultado.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    if v[1] == v[1]-1:
        print(f'{i-1}º lugar: {v[0]} com {v[1]}.')
    elif v[1] == v[1]-2:
        print(f'{i-2}º lugar: {v[0]} com {v[1]}.')
    elif v[1] == v[1]-3:
        print(f'{i-3}º lugar: {v[0]} com {v[1]}.')
    elif v[1] == v[1]-4:
        print(f'{i-4}º lugar: {v[0]} com {v[1]}.')
    elif v[1] == v[1]-5:
        print(f'{i-5}º lugar: {v[0]} com {v[1]}.')
    else:
        print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(1)




resutados = dict()
jogadores = list()
print('Valores sorteados:')
for c in range(0, 4):
    n = random.randint(1, 6)
    resutados['Jogador'+str(c+1)] = n
    jogadores.append(n)
    time.sleep(0.5)
    print(f'O {"Jogador"+str(c+1)} tirou {n}')
jogadores.sort(reverse= True)
jogar = 't'
print('Ranking dos jogadores:')
for p in range(0,4):
    print(f'{p+1}º Lugar: ', end='')
    for k, v in resutados.items():
        if v == jogadores[p] and jogar != k:
            time.sleep(0.1)
            print(k,'com',v)
            jogar = k
            break




lugar=0
jogadores={}
jogadores = {}
print('=====Valores Sorteados:')
for i in range(1, 5):
        jogadores['Jogador {}'.format(i)] = random.randint(1, 6)
        print('  Jogador {} jogou o dado e obteve o valor: {}'.format(i,jogadores['Jogador {}'.format(i)]))
        time.sleep(1)
print('='*40)
for i in range(1, 5):
    if jogadores['Jogador 1'] >= jogadores['Jogador 2'] and  jogadores['Jogador 1'] >=  jogadores['Jogador 3'] and jogadores['Jogador 1'] >= jogadores['Jogador 4'] and jogadores['Jogador 1'] != 0:
        lugar+=1
        print('Jogador 1 ficou em {}° lugar com {} no dado'.format(lugar,jogadores['Jogador 1']))
        jogadores['Jogador 1']=0
    if jogadores['Jogador 2'] >= jogadores['Jogador 1'] and  jogadores['Jogador 2'] >=  jogadores['Jogador 3'] and jogadores['Jogador 2'] >= jogadores['Jogador 4'] and jogadores['Jogador 2'] != 0:
        lugar+=1
        print('Jogador 2 ficou em {}° lugar com {} no dado'.format(lugar,jogadores['Jogador 2']))
        jogadores['Jogador 2']=0
    if jogadores['Jogador 3'] >= jogadores['Jogador 1'] and  jogadores['Jogador 3'] >=  jogadores['Jogador 2'] and jogadores['Jogador 3'] >= jogadores['Jogador 4'] and jogadores['Jogador 3'] != 0:
        lugar+=1
        print('Jogador 3 ficou em {}° lugar com {} no dado'.format(lugar,jogadores['Jogador 3']))
        jogadores['Jogador 3']=0
    if jogadores['Jogador 4'] >= jogadores['Jogador 1'] and  jogadores['Jogador 4'] >=  jogadores['Jogador 3'] and jogadores['Jogador 4'] >= jogadores['Jogador 2'] and jogadores['Jogador 4'] != 0:
        lugar+=1
        print('Jogador 4 ficou em {}° lugar com {} no dado'.format(lugar,jogadores['Jogador 4']))
        jogadores['Jogador 4']=0