import os
nome = []
preco = []
os.system("cls") # comando de limpar a tela
total = 0
qtd = 1
masmil = 0
while True:
    n = input('Nome do produto: ')
    while n.isalpha() != True:
        n = input('Invalido. Nome do produto: ')
    p = float(input('Preço: '))
    while p<0:
        p = float(input('Preço invalido. Preço: '))
    if p>1000:
        masmil += 1
    total += p
    nome.append(n)
    preco.append(p)
    continuar = input('Gostaria de comprar mais produtos? [S][N]').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Invalido. Deseja continuar? [S][N]').upper()
    if continuar == 'N':
        break
    qtd += 1
    
    
for i in range(len(nome)):
    print(nome[i], ':', preco[i])
print(f'Total = {total:.2f}')
print('Produtos que custam mais de R$1000,00 =', masmil)
barato = 0
masbarato = 0
for i in range(len(nome)):
    if i == 0:
        barato = nome[i]
        masbarato = preco[i]
    if i>0:
        if preco[i]<masbarato:
            barato = nome[i]
            masbarato = preco[i]
print('O produto mais barato foi {}, custando R${:.2f}'.format(barato, masbarato))