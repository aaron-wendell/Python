print('Gerador de PA')
numero = int(input('Primeiro termo: '))
prog = int(input("Razão: "))
cont = 1
x = 10
total = 0
while x!=0:
    total = total + x
    while cont<=total:
        print(numero,'\033[30m->\033[m', end='')
        numero += prog
        cont += 1
    print('Pausa')
    x = int(input('Quantos termos deseja mostrar a mais? '))
print('Progressao Aritmetica finalizada com {} termos mostrados'.format(total))