from ex108.utilidades import funcoes
import math

funcoes.cabecalho('CALCULADORA')

while True:
    v1 = funcoes.leiafloat('Valor 1: ')
    operacao = funcoes.matematica()
    v2 = funcoes.leiafloat('Valor 2: ')
    if operacao == '+':
        print(f'{v1} + {v2} = {v1+v2}')
        break
    elif operacao == '-':
        print(f'{v1} - {v2} = {(v1-v2)}')
        break
    elif operacao == 'x':
        print(f'{v1:.4f} x {v2:.4f} = {(v1*v2):.4f}')
        break
    elif operacao == '/':
        print(f'{v1:.4f} / {v2:.4f} = {(v1/v2):.4f}')
        break
    elif operacao == '^':
        print(f'{v1:.4f}^{v2:.4f} = {(math.pow(v1, v2)):.4f}')
        break
    else:
        print('\03331m]Operação invalida!\033m]')
