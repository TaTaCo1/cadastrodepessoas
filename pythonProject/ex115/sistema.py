import time

from ex115.Lib.interface import *
from time import sleep

cabecalho('SISTEMA ARQUIVOS V1.0')

while True:
    resposta = menu(['Listar pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])

    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema ...')
        break
    else:
        cabecalho('ERRO! Digite uma opção válida!')

    time.sleep(2)

