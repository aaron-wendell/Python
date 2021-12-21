import datetime
dici = {}
dici['nome'] = input("Nome: ")
nasc = int(input('Ano de nascimento: '))
dici['idade'] = (datetime.date.today().year - nasc)
dici['carteira'] = int(input('CTPS: '))
if dici['carteira'] != 0:
    dici['contratacao'] = int(input('Ano de contratação: '))
    dici['salario'] = float(input('Salario: R$'))
    dici['aposentadoria'] = dici['contratacao'] + 35 - nasc 
print('=-'*30)
for k, v in dici.items():
    print(f'- {k} tem o valor {v}'.capitalize())