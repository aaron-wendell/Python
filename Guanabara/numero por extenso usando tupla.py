tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
dig = int(input('Digite um valor entre 0 e 20: '))
while dig<0 or dig>20:
    dig = int(input('Digite um valor entre 0 e 20: '))
print(f'Você digitou o numero {tupla[dig]}')