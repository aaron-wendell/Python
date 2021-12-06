vetor = []

x = int(input('Digite um valor para o vetor'))
while x!=0:
    vetor.append(x)
    x = int(input('Digite um valor para o vetor'))

print(vetor)

for i in range(len(vetor)):
    if vetor[i]>0:
        vetor[i] = 1
    else:
        vetor[i] = 0

print(vetor)