jogador = {}
jogadores = list()
while True:
    jogador['nome'] = input('Nome do jogador: ').capitalize()
    jogador['partida'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    gol = []
    total = 0
    for i in range(jogador['partida']):
        gol.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}: ')))
        total += gol[i]
    jogador['gol'] = gol
    jogador['total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    cont = input('Deseja continuar: [S][N] ').upper()[0]
    while cont not in 'SN':
        cont = input('Erro! Digite apenas S ou N. Deseja Continuar: [S][N]').upper()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"PARTIDAS":>8}{"GOLS":>8}')
c = 0
for i in jogadores:
    c += 1
    print(f'{c:<4}{i["nome"]:<10}{i["partida"]:>8}{i["total"]:>8}')
print('-='*30)
while True:
    rendimento = input('Gostaria de ver o rendimento de algum jogador? [S][N]').upper()
    if rendimento == 'N':
        break
    else:
        num = int(input('Digite o numero do jogador: '))-1
        if num <= len(jogadores)-1:
            print(f'O jogador {jogadores[num]["nome"]} jogou {jogadores[num]["partida"]} partidas.')
            for i in range(jogadores[num]['partida']):
                print(f'     => Na partida {i+1}, {jogadores[num]["nome"]} fez {jogadores[num]["gol"][i]} gols')
            print(f'{jogadores[num]["nome"]} marcou um total de {jogadores[num]["total"]} gols')
        else:
            print('Jogador não encontrado.')
print('Volte Sempre :)')