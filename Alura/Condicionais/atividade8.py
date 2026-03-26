def coleta_dados():
    distancia = int(input('Digite a distancia percorrida (em km): '))

    if distancia <= 100:
        print(f'Valor do pedagio : R$10,00')
        voltar()
    elif 100 <= distancia <= 200:
        print(f'Valor do pedagio : R$20,00')
        voltar()
    else:
        print('Valor do pedagio : R$ 30,00')
        voltar()

def voltar():
    input('\nEnter pra voltar')
    main()

def main():
    coleta_dados()

if __name__ == "__main__":
    main()