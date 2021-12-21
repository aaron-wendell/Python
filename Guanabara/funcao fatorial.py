def fatorial(num, show=False):
    """=>Calcula o fatorial de um numero
    :param n = o numero a ser calculado
    :param show (opcional) = mostra a conta
    :return = O valor do fatorial de n """
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


n = int(input('Fatorial de '))
print(fatorial(n), show=True)