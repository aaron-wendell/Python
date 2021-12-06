def tamanho(a, b):
    if a>b:
        print(b)
    elif b>a:
        print(a)
    else:
        print('Os numeros sao iguais')

x = int(input('Primeiro numero: '))
y = int(input('Segundo numero: '))

tamanho(x,y)