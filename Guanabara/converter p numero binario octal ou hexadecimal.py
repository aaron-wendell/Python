import math
numero = int(input('Digite um numero para fazer a conversao: '))
opcao = int(input('Digite qual base deseja escolher\n1. Binario\n2. Octal\n3. Hexadecimal'))
if opcao == 1:
    print(bin(numero)[2:])
elif opcao == 2:
    print(oct(numero)[2:])
elif opcao == 3:
    print(hex(numero)[2:])