nome = list()
peso = list()
maspeso = menospeso = i = 0
while True:
    nome.append(input('Nome: ').capitalize())
    nome.append(float(input('Peso: ')))
    if i == 0:
        maspeso = menospeso = nome[1]
    else:
        if nome[1]>maspeso:
            maspeso = nome[1]
        if nome[1]<menospeso:
            menospeso = nome[1]
    peso.append(nome[:])
    nome.clear()
    cont = input('Deseja continuar? [S][N]').upper()
    if cont == 'S':
        i += 1
        continue
    if cont == 'N':
        break
print('Total de pessoas cadastradas: {}'.format(i+1))
print(f'Maior peso registrado: {maspeso:.2f}Kg. Peso de ', end='')
for i in peso:
    if maspeso == i[1]:
        print(f'{i[0]}', end='')
print(f'Menor peso registrado: {menospeso:.2f}Kg. Peso de ', end='')
for i in peso:
    if menospeso == i[1]:
        print(f'{i[0]}', end='')