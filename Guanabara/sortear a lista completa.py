import random
vet = []
for i in range(4):
    vet.append(input('{}º aluno: '.format(i+1).capitalize()))
print(vet)
print('Lista em ordem Alfabetica')
print(sorted(vet))
print('Lista Sorteada')
random.shuffle(vet)
print(vet)