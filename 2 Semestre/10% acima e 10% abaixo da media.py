vet = []
soma = 0
for i in range(10):
    vet.append(float(input(f'Nota {i+1}: ')))
    soma += vet[i]

media = soma/10
acima = 0
abaixo = 0
for i in range(10):
    if vet[i]>(media*1.10):
        acima += 1
    elif vet[i]<(media*0.9):
        abaixo += 1
print('Media: {}'.format(media))
print('Notas acima da media 10%: {}'.format(acima))
print('Notas abaixo da media 10%: {}'.format(abaixo))