casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o tamanho do seu salario: '))
anos = int(input('Em quantos anos deseja pagar: '))
mesada =  casa / (12*anos)
if (salario*0.3) > mesada:
    print('Sua prestação mensal é de R${:.2f}'.format(mesada))
else:
    print('Mesada negada porque sua prestação mensal seria R${:.2f}, valor acima de 30% de seu salario'.format(mesada))