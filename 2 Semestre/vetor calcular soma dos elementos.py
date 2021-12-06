vet = []
soma = 0
N = int(input('Digite a quantidade de números: '))
for i in range(N):
    vet.append(int(input('Digite os números: ')))
    soma += vet[i]
print(vet)
print(soma)
