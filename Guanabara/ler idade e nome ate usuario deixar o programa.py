nome = []
idade = []
sexo = []
while True:
    class vet:
        nome = input('Nome: ').title()
        while nome.isalpha() != True:
            nome = input('Nome invalido. Nome: ').title()
        idade = int(input('Idade: '))
        while idade<0 or idade>150:
            idade = int(input('Idade invalida. Idade: ')) 
        sexo = input('Sexo: [M][F]').upper()
        while sexo != 'M' and sexo != 'F':
            sexo = input('Sexo invalido. Sexo: [M][F]').upper()
    print(f'Nome: {vet.nome}\nIdade: {vet.idade}\nSexo: {vet.sexo}')
    nome.append(vet.nome)
    idade.append(vet.idade)
    sexo.append(vet.sexo)
    continua = input('Deseja continuar? [S][N]').upper()
    while continua != 'S' and continua != 'N':
        continua = input('Invalido. Deseja continuar? [S][N]').upper()
    if continua == 'N':
        break
maior = 0
homem = 0
mulhern = 0 
for i in range(len(idade)):
    if idade[i]>18:
        maior += 1
    if idade[i]<20 and sexo[i] == 'F':
        mulhern += 1
    if sexo[i] == 'M':
        homem += 1

print(f'''Pessoas acima de 18 anos: {maior}
Homens: {homem}
Mulheres: {(len(sexo))-homem}
Mulheres com menos de 20 anos: {mulhern}''')