class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria ):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} \n {restaurante.categoria} \n {restaurante.ativo}')

    
    

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')


restaurantes = [restaurante_praca, restaurante_pizza]

Restaurante.listar_restaurantes()




#if restaurante_praca.ativo:
#    print(f'O restaurante {restaurante_praca.nome} está ativo')
#else:
#    print(f'O restaurante {restaurante_praca.nome} está inativo')


#if restaurante_pizza.categoria == 'Fast Food':
#    print('Categoria correta')


#print(f'{restaurante_praca.nome} - {restaurante_praca.categoria}')