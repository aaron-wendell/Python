vet = []
while True:
    vet.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [N]')).upper()
    if cont in 'NÃONAO':
        break
vet.sort(reverse=True)
print("Os valores em ordem decrescente são {}".format(vet))
if 5 in vet:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao esta na lista')