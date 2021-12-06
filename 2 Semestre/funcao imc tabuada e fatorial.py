def tabuada(num):
    tab = 0
    if num>0 and num<10:
        print('Tabuada do {}'.format(num))
        for i in range(1, 11, 1):
            tab = num * i
            print(num, 'x', i,'=', tab)
    else:
        print('Numero inválido\nEscolha um numero entre 1 e 9')

def imc(p, alt):
    if peso>0 and altura>0:
        valor = p / (alt**2)
    return valor

escolha = 0
while escolha != -1:
    escolha = int(input('Escolha um numero da lista: \n1. Tabuada\n2. IMC\n3. Fatorial\n-1. Sair\n'))
    if escolha == 1:
        tab = int(input('Digite um numero para sua a tabuada: '))
        tabuada(tab)
    if escolha == 2:
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        print(f'IMC = {imc(peso, altura):.2f}')
        if imc(peso, altura)<18.5:
            print('Voce esta abaixo do peso!')
        elif imc(peso, altura)<25:
            print('Parabens! Seu peso esta ideal. Continue cuidando de sua saude ')
        elif imc(peso, altura)<30:
            print('Voce esta acima do peso. Faca uma dieta ')
        elif imc(peso, altura)<=40:
            print('Voce esta obeso. Va para a academia e faca dieta')
        elif imc(peso, altura)>40:
            print('Voce esta com obesidade morbida. Precisa buscar fazer uma cirurgia bariatrica urgente!')
    if escolha == 3:
        fatorial = int(input('Digite o numero o qual desejas saber o fatorial: '))
        
    if escolha == -1:
        print('O programa sera encerrado')
    if escolha !=-1 and escolha !=3 and escolha !=0 and escolha !=1 and escolha !=2:
        print('Numero invalido')
