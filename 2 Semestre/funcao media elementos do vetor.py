def media(vet):
    s = 0
    for i in range(5):
        s += vet[i]
    return (s/5)

vet = []
for i in range(5):
    vet.append(int(input('Numero: ')))

print('A média é', media(vet))