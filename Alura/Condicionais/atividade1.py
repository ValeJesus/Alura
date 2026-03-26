def exibir_nome_programa():
    print(
        """
        Barraca do Bruno
    """
    )

def pegar_infos():
    maças = input(f"Digite a quantidade maças vendidas: ")
    bananas = input(f"Digite quantas bananas foram vendidas: ")

    if maças > bananas:
        print("As maças tiveram mais vendas")
    elif bananas > maças:
        print("As bananas tiveram mais vendas")
    else:
        print("Houve um empate")

    executardnv()


def executardnv():
    input("\n clique qualquer tecla para executar o programa dnv ")

    main()


def main():
    exibir_nome_programa()
    pegar_infos()


if __name__ == "__main__":
    main()
