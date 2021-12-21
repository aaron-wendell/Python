pessoas = dict()
lista = list()
total = media = 0
while True:
    pessoas['nome'] = input('Nome: ').title()
    pessoas['sexo'] = input('Sexo [M][F] ').upper()[0]
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = input('Erro! Digite apenas M ou F. Sexo [M][F] ').upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    total += 1
    total += pessoas['idade']
    lista.append(pessoas.copy()) 
    pessoas.clear()
    cont = input('Deseja Continuar: [S][N]').upper()[0]
    while cont not in 'SN':
        cont = input('Erro! Digite apenas S ou N. Deseja Continuar: [S][N]').upper()[0]
    if cont == 'N':
        break
media = total / len(lista)
print('-='*30)
print(lista)
print('A) Ao todo {} pessoas foram cadastradas'.format(len(lista)))
print(f'B) A média de idade é {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for i in lista:
    if i['sexo'] in 'F':
        print(i["nome"], end='')
print('D) Lista de pessoas com idade acima da media: ', end='')
for i in lista:
    if i['idade'] > media:
        print('      ')  
        for k, v in i.items():
            print(f' {k} = {v};', end='')
        print()
print('Volte Sempre!!')