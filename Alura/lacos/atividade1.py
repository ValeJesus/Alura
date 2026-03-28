clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

def exe():

    for i, cliente in enumerate(clientes):
        print(f'cliente Nº: {i + 1} Nome : {cliente}')

    exednv()
        



def exednv():
    resposta = input('Você quer executar o programa denovo?(S ou N)')
    if resposta == 'S' or resposta == 's':
        main()
    elif resposta == 'N' or resposta == 'n':
        return
    
       
def main():
    exe()

if __name__ == "__main__":
    main()