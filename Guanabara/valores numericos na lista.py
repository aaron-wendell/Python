vet = []
while True:
    valor = int(input('Digite um valor numerico: '))
    while valor in vet:
        valor = int(input('Valor ja digitado. Digite um valor numerico: '))
    vet.append(valor)
    cont = input('Deseja continuar? [S][N]').upper()
    while cont != 'S' and cont != 'N':
        cont = input('Invalido. Deseja continuar? [S][N]').upper()
    if cont == 'N':
        break
vet.sort()
print('Valores adicionados: ', end='')
print(vet)