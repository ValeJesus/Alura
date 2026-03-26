def exibir_nome():
    print('''
    Controle de orçamento
    ''')

def coletar_dados():
    
    despesas = float(input('Digite o total de despesas do mês (R$): '))
    ValorAMais = despesas - 3000
    ValorAMenos = 3000 - despesas

    if despesas > 3000.00:
        print(f'Você ultrapassou o limite do orçamento! Você gastou {ValorAMais:.2f} a mais! ')
        # :.2f pra permitir 2 casas decimais
        voltar()

    elif despesas <= 3000.00:
        print(f'Você não ultrapassou o limite do orçamento! Você ainda pode gastar: {ValorAMenos:.2f} ')
        # :.2f pra permitir 2 casas decimais
        voltar()

def voltar():
    input('digite qualquer letra para voltar!')
    main()

def main():
    exibir_nome()
    coletar_dados()

if __name__ == "__main__":
    main()


        
