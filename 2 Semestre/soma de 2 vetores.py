vet = []
vet2 = []
soma = []
for i in range(0, 50, 1):
    vet.append(int(i))
for i in range(50, 101, 1):
    vet2.append(int(i))
print('Vetor 1:')
print(vet)
print('Vetor 2:')
print(vet2)
soma.append(vet + vet2)
print('Soma dos elementos do vetor\n', soma)
