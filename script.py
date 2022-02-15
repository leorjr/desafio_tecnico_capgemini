def create_a_ladder():

    while True:
        try:
            n = int(input('Informe a altura da escada (numérico): '))
            break
        except ValueError:
            print("Por favor, informe um valor numérico.")

    for i in range(n):
        item = i + 1
        print('*'*item)


create_a_ladder()