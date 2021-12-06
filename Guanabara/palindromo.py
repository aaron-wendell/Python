frase = input('Digite uma frase: ').strip().upper()
frase = frase.split()
junto = ''.join(frase)
inverso = ''
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]

print(f'O inverso de {junto} eh {inverso}')
if junto == inverso:
    print('Ara Ara parece que temos um palindromo!')
else:
    print('A palavra nao eh um palindromo')