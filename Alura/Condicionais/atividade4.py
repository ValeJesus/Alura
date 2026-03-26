def exibir_nome():
    print('''
    Calculo do IMC
    ''')

def coletar_dados():
    peso = float(input('Digite o seu peso(em kg): '))
    altura = float(input('Digite a sua altura(em metros): '))

    IMC = peso / (altura ** 2 )

    if IMC < 18.5:
        print(f'Você está abaixo do peso, seu IMC é: {IMC:.f2}')
        # o : --> formatar | f --> indica q é float | 2 --> número de casas decimais        
        voltar()
    elif 18.5 <= IMC < 25:
        print(f'Peso normal! seu IMC é {IMC:.2f} ')
        voltar()
    else:
        print(f'Você está acima do peso, seu IMC é {IMC:.2f}')
        voltar()

def voltar():
    input('\ndigite qualquer tecla para executar o codigo novamente')
    main()

def main():
    exibir_nome()
    coletar_dados()

if __name__ == "__main__":
    main()


