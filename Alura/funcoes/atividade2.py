def coleta():
    palavra = list(input('Digite uma palavra: '))

    numero = len(palavra)

    print(f'Sua palavra tem {numero} letras')
    print(f'\npalavra desmembrada: {palavra}')

coleta()