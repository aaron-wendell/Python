vetor = []
for i in range(5):
    vetor.append(int(input(f'Digite um valor para a posicao {i}:')))
maior = 0
menor = 0
for i in range(5):
    if i == 0:
        maior = menor = vetor[i]
    else: 
        if vetor[i]>maior:
            maior = vetor[i]
        if vetor[i]<menor:
            menor = vetor[i]
    if max(vetor) == vetor[i]:
        print(f'O maior valor eh {maior} na posicao {i}')
    if min(vetor) == vetor[i]:
        print(f'O menor numero eh {menor} na posicao {i}')
