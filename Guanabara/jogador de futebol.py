jogador = {}
jogador['nome'] = input('Nome do jogador: ')
jogador['partida'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
gol = []
total = 0
for i in range(jogador['partida']):
    gol.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}: ')))
    total += gol[i]
jogador['gol'] = gol
jogador['total'] = total
print(jogador)
print('-='*30)
for i, k in jogador.items():
    print(f'O campo {i} tem o valor {k}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partida"]} partidas.')
for i in range(jogador['partida']):
    print(f'     => Na partida {i+1}, {jogador["nome"]} fez {jogador["gol"][i]} gols')
    #print(f'     => Na partida {i+1}, {jogador["nome"]} fez {gol[i]} gols')
print(f'{jogador["nome"]} marcou um total de {jogador["total"]} gols')