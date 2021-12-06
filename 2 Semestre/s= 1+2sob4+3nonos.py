def soma(n):
    soma = 0
    for i in range(1, n+1, 1):
        soma += i/(i**2)
    return soma
n = -2
while n<=0: 
    n = int(input('Digite o valor de n: '))
    if n<=0:
        print('Valor invalido. Digite um numero acima de 0')
print('Soma = ', soma(n))