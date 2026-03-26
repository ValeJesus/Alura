def coleta_dados():
    p1 = float(input('Digite a primeira nota : '))
    p2 = float(input('Digite a segunda nota : '))
    p3 = float(input('Digite a terceira nota : '))

    media = (p1 + p2 + p3) / 3

    if media >= 7:
        print(f'Aprovado, sua media é {media:.1f}')
        voltar()
    elif 5<= media <7:
        print(f'Recuperação, sua media é {media:.1f}')
        voltar()
    else:
        print(f'Reprovado, sua media é {media:.1f}')
        voltar()

def voltar():
    input('\nEnter pra executar novamente')
    main()

def main():
    coleta_dados()


if __name__ == "__main__":
    main()