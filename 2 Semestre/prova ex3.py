# Aaron Wendell Engenharia de Software 23736
def media(altura, idade):
    soma = 0
    media = 0
    for i in range(5):
        soma += 1
        media = altura/5
    for i in range(5):
        if idade[i] > 25 and altura[i]<media:
            soma += 1
    print(media)
    print('Soma da quantidade de alunos', soma)
altura = []
idade = []
for i in range(5):
    altura.append(float(input('Digite a altura: ')))
    idade.append(int(input('Digite a idade: ')))
media(altura, idade)