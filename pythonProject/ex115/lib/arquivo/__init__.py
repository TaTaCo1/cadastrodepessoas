from ex115.lib.interface import *
def arquivo_existe(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def arquivo_criar(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def arquivo_ler(nome):
    try:
        arq = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo !')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

def cadastrar(arq, nome= 'desconhecido', idade = 0):
    try:
        abrir= open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            abrir.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registo de {nome} adicionado')
            abrir.close()



