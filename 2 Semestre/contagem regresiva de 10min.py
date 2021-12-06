minuto = 10
segundo = 60
for minuto in range(10, 0, 1) and segundo in range(60, 0, 1):
    if(minuto==10):
        print(minuto, '\n')
        break
    else:
        print(minuto, ':', segundo)
