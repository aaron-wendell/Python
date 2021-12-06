def tamanho(vet):
    maior = -99999
    menor = 999999
    for i in range(10):
        if vet[i]>maior:
            maior = vet[i]
        if vet[i]<menor:
            menor = vet[i]
    print(f'O maior numero: {maior}')
    print(f'O menor numero: {menor}')


vet = []
for i in range(10):
    vet.append(int(input('Numero: ')))

tamanho(vet)