import re

def create_a_ladder():

    while True:
        try:
            n = int(input('Informe a altura da escada (numérico): ').strip())
            break
        except ValueError:
            print("Por favor, informe um valor numérico.")

    for i in range(n):
        item = i + 1
        print('*'*item)



def validation_on_a_password():

    while True:

        password = input("Informe o password: ")

        if len(password) < 6:
            print('Password precisa ter, no mínimo, 6 caracteres')

        elif re.search(r'\d', password) == None:
            print('Favor informar, ao menos, 1 número.')

        elif re.search(r'[A-Z]', password) == None:
            print('Favor informar, ao menos, 1 letra maiúscula.')
        
        elif re.search(r'[a-z]', password) == None:
            print('Favor informar, ao menos, 1 letra minúscula.')
        
        elif re.search(r'[!@#$%^&*()\-+]', password) == None:
            print('Favor informar, ao menos, 1 caractere especial.')
        
        else:
            print('Password validado!')
            break
            
       