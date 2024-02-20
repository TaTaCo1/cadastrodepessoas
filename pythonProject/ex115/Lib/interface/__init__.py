def leiaint(msg):
    while True:
        try:
            number= int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: Por favor, difite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuário decidiu não digitar esse número.\033[m')
            return 0
        else:
            return number


def line (size = 42):
    return '-' * size


def cabecalho (txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu (lst):
    cabecalho('MENU PRINCIPAL')
    count = 1
    for item in lst:
        print(f'{count} - {item}')
        count+=1
    print(line())
    opc = leiaint('Sua Opção:')
    return opc

