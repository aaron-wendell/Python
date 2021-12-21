tabela = ('Atletico Mineiro', 'Flamengo', 'palmeiras'.title(), 'Corinthians', 'Fortaleza', 'Bragantino', 'Fluminense', 'America Mg', 'Ceara', 'Internacional', 'São Paulo', 'Atletico Go', 'Athletico Pr', 'Santos', 'Bahia', 'Juventude', 'Cuiaba', 'Gremio', 'Sport', 'Chapecoence')
print('Tabela do brasileirao: {}'.format(tabela))
print('-='*85)
time = input('Time que gostaria de consultar: ').title()
while time not in tabela:
    time = input('Time não encontrado. Time que gostaria de consultar: ').title()
if time in tabela:
    print(f'{time} esta na {tabela.index(time)+1}ª posicao no Brasileirão série A')
for i in range(len(tabela)-15):
    print(f'{i+1}º colocado: {tabela[i]}')

for i in range(16, len(tabela)):
    print(f'{i+1}º colocado: {tabela[i]}')

print('-='*85)
print('Times em ordem alfabetica:')
print(sorted(tabela))

