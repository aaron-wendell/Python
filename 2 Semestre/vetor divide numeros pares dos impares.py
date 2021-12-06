vet = []
vetpar = []
vetimpar = []
for i in range(10):
    vet.append(int(input('Digite um numero: ')))
    if vet[i]%2:
        vetimpar.append(vet[i])
    else:
        vetpar.append(vet[i])
print(vetimpar)
print(vetpar)