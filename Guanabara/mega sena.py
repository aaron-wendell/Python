from random import randint
import time
lista = []
jogos = list()
palpite = int(input('Quantos jogos deseja sortear: '))
for i in range(palpite):
    for seis in range(6):
        x = randint(1, 60)
        if x not in lista:
            lista.append(x)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print(F'SORTEANDO {palpite} JOGOS')
time.sleep(1)
for i in range(palpite):
    print(F'JOGO {i+1}: ',jogos[i])
    time.sleep(1)
print('-='*5,'< BOA SORTE! >','=-'*5)