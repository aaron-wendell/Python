real = float(input('Digite um valor em real: '))
if real <= 0:
    real = 1
    dolar = real / (5.63)
    print('Valor invalido. Considerando 1 real: ')
    print(f'1 real = {dolar:.2f} dolar')
elif real == 1:
    dolar = real/(5.63)
    print(real, 'real', f'= {dolar:.2f} dolar')

elif real <= (5.63):
    dolar = real/(5.63)
    print(real, 'reais', f'= {dolar:.2f} dolar')

else:
    dolar = real/(5.63)
    print(real, 'reais', f'= {dolar:.2f} dolar')
