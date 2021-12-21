print('-'*40)
print('{:^40}'.format('listagem de preços').upper())
print('-'*40)
tupla = ('lápis'.capitalize(), 1.75, 'borracha'.capitalize(), 2, 'caderno'.capitalize(), 15.9, 'estojo'.capitalize(), 8.1, 'transferidor'.capitalize(), 4.2, 'compasso'.capitalize(), 9.99, 'mochila'.capitalize(), 120.68, 'caneta'.capitalize(), 0.9, 'livro'.capitalize(), 34.94)
for i in range(len(tupla)):
    if i%2==0:
        print(tupla[i], end='')
        for x in range(30-len(tupla[i])):
            print('.', end='')
    if i%2:
        print('R$ {:.2f}'.format(tupla[i]))

print('-'*40)
