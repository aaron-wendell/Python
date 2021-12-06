import random
numero = random.randint(0, 5)
suposicao = int(input('Digite um valor entre 0 a 5: '))
while suposicao>5 or suposicao<0:
    suposicao = int(input('Valor invalido. Digite um valor entre 0 a 5: '))
if suposicao == numero:
    print('Acertou! Parabens! O numero escolhido realmente era {} '.format(numero))
else:
    print('Errou! O número escolhido era {} e voce escolheu {}'.format(numero, suposicao))