def coleta():
    num = input('Digite os valores : ').split() # --> divide essa bomba em uma lista
    total = sum(map(float, num ))

    print(f'O total das vendas foi : {total}')

coleta()