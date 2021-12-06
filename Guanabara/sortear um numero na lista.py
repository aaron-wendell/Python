import random
vet = []
for i in range(4):
    vet.append(input('{}º aluno: '.format(i+1)))
print(random.choice(vet))