distancia = float(input('Digite a distancia que pretendes percorrer em km/h: '))
while distancia<0:
    distancia = float(input('Distancia inválida. Digite a distancia que pretendes percorrer em km/h: '))
if distancia<=200:
    passagem = distancia*0.5
    print('O preço da viagem é R${:.2f}'.format(passagem))
else:
    passagem = distancia*0.45    
    print('O preço da viagem é R${:.2f}'.format(passagem))
