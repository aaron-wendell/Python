def hello(meunome, idade):
    print('Olá %s!\nSua idade é %d'%(meunome, idade))

hello('Ana', 25)

nome = input('Nome: ')
idade = int(input('Idade: '))
hello(nome, idade)