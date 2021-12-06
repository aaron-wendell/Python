valor = float(input('Valor do produto: '))
pag = int(input('Escolha a forma de pagamento.\n1. Dinheiro ou Cheque\n2. Cartao '))
while pag>2 or pag<1:
    pag = int(input('Opcao invalida.\nEscolha a forma de pagamento.\n1. Dinheiro\n2. Cartao '))
if pag == 1:
    valor = valor * 0.9
    print(valor)
if pag == 2:
    dividir = int(input('Gostaria de dividir em quantas vezes? '))
    while dividir<1:
        dividir = int(input('Divisao invalida. Gostaria de dividir em quantas vezes? '))
    if dividir == 1:
        valor = valor * 0.95
        print('Valor total =', valor)
    elif dividir == 2:
        print('Valor total =', valor)
    else:
        valor = valor + (dividir*0.2)
        print('Valor total =', valor)