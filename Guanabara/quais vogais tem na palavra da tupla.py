palavras = ('aprender', 'programa', 'python', 'curso', 'programador', 'linguagem', 'estudar')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aiueo':
            print(letra, end=' ')