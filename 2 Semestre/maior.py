def tamanho(vet):
    menor = 999999
    for i in range(10):
        if vet[i]<menor:
            menor = vet[i]
    print(f'O menor numero: {menor}')
    
vet = []
for i in range(10):
    vet.append(int(input('Numero: ')))

tamanho(vet)