
telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
print(telefones)
def converter():

    convertidos = []
    
    for telefone in telefones:
        telefone_int = int(telefone)
        convertidos.append(telefone_int)
    
    if len(convertidos) == len(telefones):
        print('Convertidos com sucesso! ')
    else:
        print("A conversão falhou")

converter()
print(telefones)