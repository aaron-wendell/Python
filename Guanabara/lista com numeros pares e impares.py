lista = [[], []]
for i in range(7):
    x = int(input('Valor: '))
    if x%2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
print('Os numeros pares digitados sao os seguintes:', lista[0])
print('Os numeros impares digitados sao os seguintes:', lista[1]) 