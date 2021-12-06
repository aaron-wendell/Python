numero = int(input('Digite o numero: '))
numero2 = int(input('Digite o numero: '))
numero3 = int(input('Digite o numero: '))


if  numero>numero2>numero3:
    print(numero, numero2, numero3)

elif numero2>numero3>numero:
    print(numero2, numero3, numero)

elif numero2>numero>numero3:
    print(numero2, numero, numero3)
else:
    print(numero3, numero2, numero)
