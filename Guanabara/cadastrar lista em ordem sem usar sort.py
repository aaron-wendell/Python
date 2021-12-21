vet = []
for i in range(5):
    n = int(input(f'Valor {i+1}: '))
    if i == 0 or n>vet[i-1]:
        print('Valor foi adicionado ao final da lista')
        vet.append(n)
    else:
        pos = 0
        while pos<len(vet):
            if n<=vet[pos]:
                vet.insert(pos, n)
                print(f'Valor foi adicionado na posição {i} da lista')
                break
            pos += 1

print('=-'*30)
print('Os valores digitados foram', vet)