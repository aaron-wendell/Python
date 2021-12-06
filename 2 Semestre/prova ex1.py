# Aaron Wendell Engenharia de Software 23736
nome = input('Digite o nome do funcionario: ')
salario = float(input('Digite o salario do funcionario: '))
while salario < 0:
    print('Salario inválido. Digite novamente o valor do salario')
    salario = float(input('Digite o salario do funcionario: '))
filhos = int(input('Digite o numero de filhos do funcionario: '))
while filhos < 0:
    print('Numero de filhos inválido. Digite novamente o numero de filhos')
    filhos = int(input('Digite o numero de filhos do funcionario: '))
nsal = 0
print('Nome:', nome)
print('Numero de filhos:', filhos)
if filhos == 0:
    nsal = salario * 1.10
elif filhos < 3:
    nsal = salario * 1.20
elif filhos >= 3:
    nsal = salario * 1.25
print('Salario: {:.2f}'.format(nsal))