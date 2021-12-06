maior = -999999999
menor = 999999999
vet = []
for i in range(20):
    vet.append(int(input('Digite um valor: ')))
    if vet[i]>maior:
        maior = vet[i]
    if vet[i]<menor:
        menor = vet[i]
print(vet)
print(f'O maior valor do vetor foi {maior} e o menor valor foi {menor}')