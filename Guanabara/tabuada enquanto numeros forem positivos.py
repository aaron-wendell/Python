def tab(num):
    for i in range(10):
        print(f'{num} x {i+1} = {num*(i+1)}')

while True:
    numero = int(input('Digite um numero natural para ver sua tabuada '))
    if numero < 0:
        break
    tab(numero)
