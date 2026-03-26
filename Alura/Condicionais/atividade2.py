def exibir_nome():
    print ('''
    Tempo Total da Camila
    ''')

def obter_infos():
    DiasA = int(input(f'\nInforme os dias para a atividade A: '))
    DiasB = int(input(f'\nInforme os dias para a atividade B: '))
    DiasC = int(input(f'\nInforme os dias para a atividade C: '))
    total = DiasA + DiasB + DiasC
    
    if DiasA < 0 or DiasB < 0 or DiasC < 0:
        print('O numero de dias não pode ser negativo ')
        ExeDnv()
    
    else:
        print(f'O tempo total do projeto foi de {total} Dias')
        ExeDnv()

    


def ExeDnv():
    print('\nDigite qualquer tecla para executar o programa novamente')

def main():
    exibir_nome()
    obter_infos()

if __name__=="__main__":
    main()