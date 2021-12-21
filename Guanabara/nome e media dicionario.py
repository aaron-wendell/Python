dic = dict()
dic['nome'] = input('Nome: ')
dic['média'] = float(input(f'Média de {dic["nome"]}: '))
if dic['média']>=6:
    dic['situacao'] = 'Aprovado'
else:
    dic['situacao'] = 'Reprovado'
for k, v in dic.items():
    print(f'{k} é igual a {v}'.capitalize())