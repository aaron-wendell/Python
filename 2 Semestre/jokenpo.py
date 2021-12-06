import random
import time
vet = ['Pedra', 'Papel', 'Tesoura']
sorteio = random.randint(0, 2)
print(sorteio)
jokenpo = int(input('Escolha sua jogada\n0. \033[30;42mPedra\033[m\n1. \033[4;33;44mPapel\033[m\n2. \033[41mTesoura\033[m '))
print('JO')        
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!')
time.sleep(0.5)
print(vet[jokenpo],' x ',vet[sorteio])
if jokenpo == 0:
    if sorteio == 0:
        print('Empate')
    elif sorteio == 1:
        print('Voce perdeu!')
    elif sorteio == 2:
        print('Voce ganhou!')
if jokenpo == 1:
    if sorteio == 1:
        print('Empate')
    elif sorteio == 0:
        print('Voce ganhou! ')
    elif sorteio == 2:
        print('Voce perdeu')
if jokenpo == 2:
    if sorteio == 1:
        print('Voce ganhou')
    elif sorteio == 0:
        print('Voce perdeu! ')
    elif sorteio == 2:
        print('Empate')