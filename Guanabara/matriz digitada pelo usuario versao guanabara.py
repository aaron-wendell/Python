mat = [[0,0,0], [0,0,0], [0,0,0]]
for linha in range(3):
    for coluna in range(3):
        mat[linha][coluna] = int(input('Digite o valor para a posicao[{}][{}]'.format(linha, coluna)))
print('=-'*30)
for linha in range(3):
    for coluna in range(3):
        print(f'[{mat[linha][coluna]:^5}]',end='')
    print()