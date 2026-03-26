def coleta():
    numero = int(input('Digite um número inteiro: '))

    if numero % 2 == 0:
        print('O número é par')
        voltar()
    else:
        print('O numero é impar')
        voltar()


def voltar():
    input('\nDigite enter p voltar')
    main()

def main():
    coleta()

if __name__ == "__main__":
    main()