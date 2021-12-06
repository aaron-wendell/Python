vet = []
soma = 0
n = 0
alunos = int(input('Informe a quantidade de alunos: '))
for i in range(alunos):
    vet.append(int(input('Informe a nota da prova do aluno {} '.format(i+1))))
    soma += vet[i]
    media = soma/alunos
    if vet[i] > media: 
        n += 1
print('A media da sala foi de {}'.format(media))
print('A soma de notas acima da media é {}'.format(soma))