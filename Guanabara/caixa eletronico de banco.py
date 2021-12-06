print('=' * 30)
print('{:^30}'.format('Banco Itau'))
print('='*30)
valor = int(input('Quanto desejas sacar: R$'))
cedula = 200
total = valor
totcedulas = 0
while True:
    if total>=cedula:
        total -= cedula
        totcedulas += 1
    else:
        if totcedulas>0:
            print(f'Total de {totcedulas} cédulas de R${cedula}') 
        elif cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totcedulas = 0
        if total == 0:
            break
print('Tenha um bom dia e volte sempre ao Banco Itau')
