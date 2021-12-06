def partrip(vet):
    vet2 = []
    for i in range(10):
        if i%2==0:
            vet2.append(int(vet[i]*2))
        else:
            vet2.append(int(vet[i]*3))
    return vet2

vet = []
for i in range(10):
    vet.append(int(input('Digite um valor: ')))
print(partrip(vet))