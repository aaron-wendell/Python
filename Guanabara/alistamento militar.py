import datetime
ano = datetime.date.today().year
mes = datetime.date.today().month
dia = datetime.date.today().day
print(f'Hoje eh {dia} do {mes} de {ano}')
anonasc = int(input('Ano do seu nascimento: '))
while anonasc > ano or anonasc<1900:
    anonasc = int(input('\033[31mAno invalido. Digite o ano do seu nascimento: \033[m'))
anox = ano - anonasc
mesnasc = int(input('Mes do seu nascimento: '))
while mesnasc>12 or mesnasc<1:
    mesnasc = int(input('\033[31mMes invalido. Digite o mes do seu nascimento: \033[m'))
mesx = mes - mesnasc
dianasc = int(input('Dia do seu nascimento: '))
if mesnasc<7 and mesnasc%2 == 0:
    while dianasc>30 or dianasc<1:
        dianasc = int(input('\033[31mDia invalido. Digite o dia do seu nascimento: \033[m'))
    while dianasc == 2 and anonasc%4 != 0 and dianasc>28:
        dianasc = int(input('\033[31mDia invalido. Digite o dia do seu nascimento: \033[m'))
    while dianasc == 2 and anonasc%4 == 0 and dianasc>29:
        dianasc = int(input('\033[31mDia invalido. Digite o dia do seu nascimento: \033[m'))
elif mesnasc<=7 and mesnasc%2 != 0:
    while dianasc>31 or dianasc<1:
        dianasc = int(input('\033[31mDia invalido. Digite o dia do seu nascimento: \033[m'))
elif mesnasc>7 and mesnasc%2 == 0:
    while dianasc>31 or dianasc<1:
        dianasc = int(input('\033[31mDia invalido. Digite o dia do seu nascimento: \033[m'))
elif mesnasc>7 and mesnasc%2 != 0:
    while dianasc>30 or dianasc<1:
        dianasc = int(input('\033[31mDia invalido. Digite o dia do seu nascimento: \033[m'))
diax = dia - dianasc
if diax<0:
    mesx = diax - mesx
if mesx<0:
    anox = mesx - anox
if anox<0:
    diax = anox - mesx
if anox == 18:
    print('\033[33mVoce esta na idade de se alistar\033[m')
    if mesx>0 and dia == 0:
        print('E esta {} meses atrasado! '.format(mesx))
    if mesx>0 and diax>1:
        print(f'E esta {mesx} meses e {diax} dias atrasado!')
if anox>18:
    print('\033[31mVoce está atrasado!\033[m')
    if mesx>0 and dia == 0:
        print('Ja devia ter se alistado há {} meses!'.format(mesx))
    if mesx>0 and dia > 0:
        print(f'Ja devia ter se alistado há {mesx} meses e {diax} dias!')
    if anox>0 and mesx>0 and dia > 0:
        print(f'Ja devia ter se alistado há {anox} anos, {mesx} meses e {diax} dias!')
    if anox>0 and mesx==0 and dia == 0:
        print(f'Ja devia ter se alistado há {anox} anos!')
    if anox>0 and mesx>0 and dia == 0:
        print(f'Ja devia ter se alistado há {anox} anos, {mesx} meses')     
    if anox>0 and mesx == 0 and dia > 0:
        print(f'Ja devia ter se alistado há {anox} anos e {diax} dias!')   
if anox<18:
    print('\033[32mVocê ainda nao pode se alistar\033[m')
    if mesx>0 and dia == 0:
        print('Fica sossegado que ainda te falta {} meses pra voce poder pegar em uma arma!'.format(mesx))
    if mesx>0 and dia > 0:
        print(f'Fica sossegado que ainda te falta {mesx} meses e {diax} dias pra voce poder pegar em uma arma!')
print(anox, mesx, diax)

#Querer complicar demais acabou destruindo meu codigo, algum dia arrumo ele