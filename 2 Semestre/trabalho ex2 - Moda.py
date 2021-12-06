# Aaron Wendell 23736 Engenharia de Software
import statistics
vet = []
tamanho = int(input('Digite o numero de elementos do vetor: '))
while tamanho<2:
  tamanho = int(input('Digite o numero de elementos do vetor, seja ele ao menos igual a 2: '))
for i in range(tamanho):
    x = int(input('Digite um numero para o vetor: '))
    vet.append(x)

def moda(vet):
  if len(statistics.multimode(vet)) > 1:
    print('Não há moda')
  else:
    print('A moda é', statistics.mode(vet))

moda(vet)

