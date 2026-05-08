from restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('pelesenha', 67)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()