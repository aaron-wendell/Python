def ficha(nome="<desconhecido>", gol=0):
    print(f'O jogador {nome} fez {gol} gols no campeonato')


jogador = input('Nome do jogador: ').capitalize()
gols = input('Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.isalpha() != True:
    jogador="<desconhecido>"
ficha(jogador, gols)