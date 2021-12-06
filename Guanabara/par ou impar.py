import random
def parimpar(num, comp, ip):
    if (num+comp) %2 != 0 and ip == 'I':
        return 1
    elif (num+comp) %2 == 0 and ip == 'P':
        return 2
    else:
        return 0
print('Jogo do par ou impar')
vit = 0
while True:
    comp = random.randint(0, 10)
    numero = int(input('Digite um valor entre um e dez. '))
    while numero<0 or numero>10:
        numero = int(input('Valor invalido. Digite um valor entre um e dez. '))
    ip = input('Par ou impar? [P] ou [I]: ').upper()
    while ip != 'P' and ip != 'I':
        ip = input('Invalido. Par ou impar? [P] ou [I]: ').upper()
    if parimpar(numero, comp, ip) == 0:
        print(f'{numero} + {comp} = {numero+comp}')
        if ip == 'P':
            print('Um numero impar, diferente do que voce supos. \033[31mDerrota')
        else:
            print('Um numero par, diferente do que voce supos. \033[31mDerrota')
        break
    elif parimpar(numero, comp, ip) == 1:
        print(f'{numero} + {comp} = {numero+comp}\nUm numero impar, assim como você supos. \033[32mVitoria!\033[m')
        vit += 1
    elif parimpar(numero, comp, ip) == 2:
        print(f'{numero} + {comp} = {numero+comp}\nUm numero par, assim como voce supos. \033[32mVitoria!\033[m')
        vit += 1
print(f'GAME OVER\033[m\nVoce finalizou o jogo com {vit} vitorias')