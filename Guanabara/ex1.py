num=1
while(num!=0):
    num = int(input('Qual numero? '))
if(num==0):
    nome = input('Qual seu nome? ')
    print('Boas vindas,', nome)
dia = int(input('Dia = '))
mes = input('Mes = ')
ano = int(input('Ano = '))
print(nome+' nasceu no dia ',dia, 'de ',mes,'de', ano)