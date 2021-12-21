def linha(tam=42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print(linha())
    opcao = leiaint('Sua opcao: '.title())
    return opcao

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

def arquivoexiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    return True

def criararquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    print(f'Arquivo {arquivo} criado com sucesso!')


def lerarquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('Pessoas cadastradas'.upper())
        print('Nome', end='')
        print('Idade'.center(50))
        for linha in a:
            dado = linha.split('; ')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<28}{dado[1]}')
    finally:
        a.close()

def cadastrar(arquivo, nome='<desconhecido>', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'\n{nome}; {idade}')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()