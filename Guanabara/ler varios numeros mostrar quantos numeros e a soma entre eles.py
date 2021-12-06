soma = 0
cont = 0
while True:
    valor = int(input('Digite um valor. Digite 999 para finalizar o programa. '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print(f'A soma dos {cont} valores digitados eh {soma}')