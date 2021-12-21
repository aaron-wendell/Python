array = []
for i in range(4):
    array.append(int(input('Digite um valor: ')))

tupla = (array[0], array[1], array[2], array[3])    
print(tupla)
if 9 in tupla:
    print('O valor 9 apareceu {} vezes'.format(tupla.count(9)))
else:
    print('O valor 9 não está na tupla')    
if 3 in tupla:
    print(f'O valor 3 aparece a primeira vez na tupla na posicao {tupla.index(3)+1}')
else:
    print('O valor 3 não aparece na tupla')
print('Os valores pares na tupla: ', end='')
for i in range(4):
    if tupla[i]%2==0:
        print(tupla[i],'', end='')
