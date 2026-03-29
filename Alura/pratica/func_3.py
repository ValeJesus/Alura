def contarvogais(texto):
    vogais = 'aeaeiouáéíóúàâêôãõüAEIOUÁÉÍÓÚÀÂÊÔÃÕÜiou'
    contador = 0
    for v in texto : 
        
        if v in vogais:
            contador += 1

    print(f'A quantidade de vogais no seu texto é: {contador}')


def msg():
    print('Não há vogais nesse texto')