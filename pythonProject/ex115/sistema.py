from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

cabecalho('SISTEMA ARQUIVOS V1.0')

arq = 'dados_sistema'

if not arquivo_existe(arq):
    arquivo_criar(arq)

while True:
    resposta = menu(['Listar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        arquivo_ler(arq)

    elif resposta == 2:
        # opção para cadastrar uma nova pessoa do no sistema
        cabecalho('NOVO CADASTRO')
        nome = input('Nome:')
        idade = leiaint('Idade:')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        # Opção para sair do sistema
        cabecalho('Saindo do sistema ...')
        break

    else:
        # digitou uma opção errada.
        cabecalho('ERRO! Digite uma opção válida!')

    sleep(2)
