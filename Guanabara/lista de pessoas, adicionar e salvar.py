from ex108.utilidades.funcoes import *
from time import sleep

arquivo = 'lista de pessoas.txt'

if not arquivoexiste(arquivo):
    criararquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Le arquivo
        cabecalho('Opcao 1')
        lerarquivo(arquivo)
    elif resposta == 2:
        #escreve no arquivo
        cabecalho('Opcao 2')
        nome = input('Nome: ').title()
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Encerrando o sistema... Ate a proxima')
        break
    else:
        print('\033[31mOpcao invalida\033[m')
    sleep(1)

