def coleta():
    horas = int(input('Digite a hora atual (0-23h): '))

    if horas <= 12:
        print('Bom dia!')
    elif 12 < horas <= 18:
        print('Boa tarde!')
    else:
        print('Boa noite!')

coleta()