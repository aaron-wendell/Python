def leiaint(msg='Digite um numero inteiro: '):
    print('-'*30)
    while True:
        num = input(msg)
        try:
            num = int(num)
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mErro. O usuario decidiu nao digitar esse valor.\033[m')
            return 0
        return num

def leiafloat(msg='Digite um numero real: '):
    print('-'*30)
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mErro. O usuario decidiu nao digitar esse valor.\033[m')
            return 0
        return num

n = leiaint('Digite um numero: ')
f = leiafloat()
print('O valor inteiro digitado foi {} e o valor real digitado foi {:.2f}.'.format(n, f))

