def coletar_dados():
    a1 = int(input('Digite o ano de nascimento: '))
    a2 = int(input('\n Digite o ano atual: '))

    idade = a2 - a1

    print(f'A idade atual é: {idade}')
    executardnv()

def executardnv():
    resp = input('\nVocê deseja executar o programa novamente? (S ou N)')
    if resp == 'S' or resp == 's':
       main()
    elif resp == 'N' or resp == 'n':
       exit()
    else:
       print('\nResposta invalida!')
       executardnv()

def main():
   coletar_dados()
   executardnv()

main()
