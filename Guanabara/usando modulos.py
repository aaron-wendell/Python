from ex108 import moeda


p = input('Digite o preco: R$')

print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
porcentagem = int(input('Porcentagem a qual deseja ver o numero aumentado e diminuido: '))

print(f'{moeda.moeda(p)} aumentado em {porcentagem}% é {moeda.aumentar(p, porcentagem, False)}')
print(f'{moeda.moeda(p)} diminuido em {porcentagem}% é {moeda.diminuir(p, porcentagem, False)}')