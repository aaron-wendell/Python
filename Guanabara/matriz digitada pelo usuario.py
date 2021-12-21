mat = list()
for i in range(3):
    for o in range(3):
        mat.append(int(input('Digite um valor para a posição [{}][{}]: '.format(i+1, o+1))))
print('Matriz:')
k = 1
for i in mat:
    k += 1
    if k%3 == 0:
        print('[',i,']')
    else:
        print('[',i,']', end='')

