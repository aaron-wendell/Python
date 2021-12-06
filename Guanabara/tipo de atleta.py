from datetime import date 
ano = date.today().year
nasc = int(input('Ano de nascimento: '))
while nasc > ano or nasc<1900:
    nasc = int(input('\033[31mAno invalido. Digite o ano do seu nascimento: \033[m'))
idade = ano - nasc
if idade<=9:
    print('Atleta mirim')
elif idade<=14:
    print('Atleta infantil')
elif idade<=18:
    print('Atleta junior')
elif idade<=20:
    print('Atleta senior')
else:
    print('Atleta master')