numero = int(input('Digite o valor inicial: '))
prog = int(input("Quantos passos: "))
an = numero + 9*prog 
for i in range(numero, an+prog, prog):
    print(i, end='->' )
print('The end')