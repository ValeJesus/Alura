def coleta():
    renda = int(input(' Digite o valor da sua renda mensal: '))
    parcela = int(input('digite o valor da parcela desejada: '))


    porcentagem = renda * 0.30

    if renda > 2000 and porcentagem < parcela:
        print(f'Emprestimo aprovado')
        voltar()
    elif renda < 2000:
        print(f'Emprestimo negado: Renda abaixo de R$2000,00')
        voltar()
    elif porcentagem < parcela:
        print(f'Emprestimo negado: Parcela acima de 30% da renda')
        voltar()

def voltar():
    input('Enter pra voltar')
    main()

def main():
    coleta()

if __name__ == "__main__":
    main()