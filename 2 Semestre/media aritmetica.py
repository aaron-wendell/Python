i = 0
numero = []
cont = soma = 0
for i in range(10):
    x = int(input('Entre com um numero par: \n'))
    if x%2==0:
        cont += 1
        soma += x
if cont>0:
    media = soma/cont
    print ('A media dos numeros pares eh', media)
else:
    print("Nao foi digitado numeros pares")