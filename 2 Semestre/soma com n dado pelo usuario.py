i=2
j=3
soma = 0
n = 0
while n<i:
    n = int(input('Digite um valor para o n para fazer a seguinte soma: 2/3 + 3/5 + 4/7 + 5/9 + … + n/m\n'))
    if n<i:
        print('Digite um numero valido')
else:
    while i<=n:
        i += 1 
        j += 2
        soma += i/j
    print('A soma é', soma)