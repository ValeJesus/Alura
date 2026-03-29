

def limpar(cpf):
    caracteres = '1234567890'
    for c in cpf :
        if c not in caracteres:
            print ('Erro: O CPF deve conter apenas números.: ')
    


def contar(cpf):
    quantidade = len(cpf)
    if quantidade == 11:
        print(f'CPF Válido, contém {quantidade} caracteres! ')
    else:
        print(f'O CPF invalido! ele deve conter 11 caracteres! o que voce inseriu tem {quantidade} ')
        



    



