numero = input('Digite um numero de 0 a 9999: ')
while int(numero)<0 or int(numero)>9999:
    print('Valor invalido. Digite um valor de 0 a 9999: ')
    numero = input('Digite um numero de 0 a 9999: ')
numero = numero.strip()
if int(numero)<10 and int(numero)>=0:
    print('Unidade:', numero[0])
elif int(numero)>9 and int(numero)<100:
    print('Dezena:', numero[0])
    print('Unidade:', numero[1])
elif int(numero)>99 and int(numero)<1000:
    print('Centena:', numero[0])
    print('Dezena:', numero[1])
    print('Unidade:', numero[2])
elif int(numero)>999 and int(numero)<10000:
    print('Milhar:', numero[0])
    print('Centena:', numero[1])
    print('Dezena:', numero[2])
    print('Unidade:', numero[3])
