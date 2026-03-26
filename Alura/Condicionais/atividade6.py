def exibir_nome():
    print('''
        Controle de acesso
    ''')

def coleta_de_dados():
    horas = int(input('Digite a hora atual (Formato em horas): '))

    if horas >= 18 or horas <= 8:
        print('Acesso negado.')
        voltar()
    else:
        print('Acesso permitido')
        voltar()


def voltar():
    input('\nDigite qualquer tecla para executar o programa denovo: ')
    main()

def main():
    exibir_nome()
    coleta_de_dados()

if __name__ == "__main__":
    main()