anime = {'titulo': 'ドラゴンボール',
        'ano': 1984,
        'autor':    '明鳥山'
}
anime['episodios'] = 284
print(anime.values())
print(anime.keys())
for k, v in anime.items():
    print(f'O {k} é {v}')

