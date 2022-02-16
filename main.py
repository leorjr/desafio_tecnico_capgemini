import re
from funcoes.functions import create_a_ladder, validation_on_a_password

def init():

    print('*'*20)
    print('Informe qual função deseja executar: ')
    print('')
    print('1. Criação de uma escada, baseada no valor n passado;')
    print('2. Validação de um password inputado pelo usuário;')
    print('')
    res = int(input('Digite 1 ou 2: '))
    print('*'*20)
    print('')

    if res == 1:
        create_a_ladder()
    elif res == 2:
        validation_on_a_password()
    else:
        print('Opção inválida')

init()


