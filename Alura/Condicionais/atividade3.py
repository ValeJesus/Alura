def ExibirNome():
    print('''
    Verificação de temperatura
    ''')

def ColetaDados():
    temperatura = int(input('Digite a temperatura atual: '))

    if temperatura > 25:
        print('Alerta! Temperatura acima do limite permitido! ')
        exeDnv()
    else:
        print(f'A temperatura está abaixo do limite!')
        exeDnv()
        
def exeDnv():       
    input('\n Digite qualquer tecla para executar o programa novamente')
    main()

def main():
    ExibirNome()
    ColetaDados()

if __name__ == "__main__":
    main()