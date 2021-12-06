def media(vet):
    soma = 0
    for i in range(10):
        if i%2!=0:
            soma += vet[i]
    media = soma/5
    return media
vet = []
for i in range(10):
    vet.append(int(input('Numero: ')))

print(media(vet))