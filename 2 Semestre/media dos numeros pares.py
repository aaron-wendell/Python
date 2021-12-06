i = 0
numero = []
cont = soma = 0
x = int(input('Entre com um numero par: \n'))
while x!=0:
    if x%2==0:
        cont += 1
        soma += x
    x = int(input('Entre com um numero par: \n'))
    
if cont>0:
    media = soma/cont
    print ('A media dos numeros pares eh {}'.format(media))
else:
    print("Nao foi digitado numeros pares")