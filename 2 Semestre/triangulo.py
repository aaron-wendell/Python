n1 = int(input('Digite a base do triangulo: '))
n2 = int(input('Digite o lado direito do triangulo: '))
n3 = int(input('Digite o lado esquerdo do triangulo: '))

if n1+n2 > n3 and n1+n3 > n2 and n2 + n3 > n1:
    if n1 == n2 == n3:
        print('Triangulo equilatero')
    elif n1 != n2 != n3:
        print('Triangulo escaleno')
    else:
        print('Triangulo isosceles')
else:
    print('Nao é possivel formar um triangulo com esses valores')