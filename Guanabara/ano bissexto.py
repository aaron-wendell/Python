import datetime
ano = int(input('Digite o ano. Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano%4==0:
    print('O ano {} é bisexto'.format(ano))
else:
    print('O ano {} não é bisexto'.format(ano))