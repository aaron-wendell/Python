velocidade = float(input('Digite a velocidade do carro em km/h: '))
while velocidade<0 or velocidade>800:
    velocidade = float(input('Velocidade inválida. Digite a velocidade do carro em km/h: '))
if velocidade>80:
    multa = (velocidade-80)*7
    print('Voce foi multado em R${:.2f}'.format(multa))