estoque_1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque_2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

estoque_junto = sorted(list(estoque_1 + estoque_2))
estoque_final = tuple(estoque_junto)


print(f'Estoque combinado: \n {estoque_final}')