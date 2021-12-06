dias = int(input('Quantos dias alugastes o carro? '))
km = int(input('Quantos km percorreste? '))
aluguel = dias * 60 + 0.15 * km
print(f'Valor do aluguel = R${aluguel}')