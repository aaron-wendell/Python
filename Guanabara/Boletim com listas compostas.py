nome = list()
i = 1
soma = 0
while True:
    n = (input('Nome: '))
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    soma = n1 + n2
    media = (soma/2)
    nome.append([n, [n1, n2], media])
    cont = input("Quer continuar? [S][N]")
    if cont in 'Nn':
        break
    i += 1
print('-='*30)    
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for x, a in enumerate(nome):
    print(f'{x+1:<4}{a[0]:<10}{a[2]:>8.1f}')
mostrar = 1000
while mostrar != 999:
    mostrar = int(input('Mostrar nota de qual aluno? [999 para interromper]: '))
    if mostrar <= len(nome)-1:
        print(f'Notas de {nome[mostrar][0]} sao: {nome[mostrar][1]}')
print('Volte Sempre'.upper())