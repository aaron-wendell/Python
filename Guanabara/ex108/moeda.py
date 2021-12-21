def dobro(valor = 0, formato = False):
    """=> Calcula o dobro do valor
    param: valor = recebe o valor o qual sera dobrado
    param: formato (opcional) = se o valor sera convertido ao padrao da moeda brasileira"""
    while valor.isnumeric() != True:
        valor = input('\033[31mValor inválido. Digite o valor que deseja diminuir: \033[m')
    valor = float(valor)
    dob = valor * valor
    return dob if formato is False else moeda(dob)


def metade(valor = 0, formato = False):
    """=> Calcula a metade do valor
    param: valor = recebe o valor o qual sera dividido em 2
    param: formato (opcional) = se o valor sera convertido ao padrao da moeda brasileira"""
    while valor.isnumeric() != True:
        valor = input('\033[31mValor inválido. Digite o valor que deseja diminuir: \033[m')
    valor = float(valor)
    met = valor / 2
    return met if formato is False else moeda(met)


def diminuir(valor = 0, menos = 0, formato = False):
    """=> Calcula o valor diminuido em certa porcentagem
    param: valor = recebe o valor o qual sera reduzido
    param: menos = recebe a porcentagem em que será atribuido o desconto
    param: formato (opcional) = se o valor sera convertido ao padrao da moeda brasileira"""
    while valor.isnumeric() != True:
        valor = input('\033[31mValor inválido. Digite o valor que deseja diminuir: \033[m')
    while menos.isnumeric() != True:
        menos = input('\033[31mPorcentagem invalida. Digite a porcentagem em que desejas diminuir: \033[m')
    valor = float(valor)
    menos = float(menos)
    diminuido = valor - (valor * menos/100)
    return diminuido if formato is False else moeda(diminuido)


def aumentar(valor = 0, aumentar = 0, formato = False):
    """=> Calcula o valor diminuido em certa porcentagem
    param: valor = recebe o valor o qual sera aumentado
    param: menos = recebe a porcentagem em que recebera o aumento
    param: formato (opcional) = se o valor sera convertido ao padrao da moeda brasileira"""
    while valor.isnumeric() != True:
        valor = input('\033[31mValor inválido. Digite o valor que deseja aumentar: \033[m')
    while aumentar.isnumeric() != True:
        aumentar = input('\033[31mPorcentagem invalida. Digite a porcentagem em que desejas aumentar: \033[m')
    valor = float(valor)
    aumentar = float(aumentar)
    aumentado = valor + (valor * aumentar/100)
    return aumentado if formato is False else moeda(aumentado)


def moeda(valor = 0, moeda='R$', formato = False):
    """=> Converte o valor ao padrão da moeda brasileira
    param: valor = recebe o valor o qual sera convertido a base decimal de '.' para ','
    param: moeda = recebe a moeda na qual será apresentada o valor
    param: formato = se o valor sera convertido ao padrao da moeda brasileira"""
    while valor.isnumeric() != True:
        valor = input('\033[31mValor inválido. Digite o valor que deseja aumentar: \033[m')
    return (f'{moeda}{valor:.2f}'.replace('.', ','))