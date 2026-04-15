despensa = ['açucar', 'café', 'pão', 'feijão', 'farinha']

item = input('Digite o item que você quer verificar: ')

     
if item in despensa:
    print('\nO item não precisa ser comprado')
else:
    print(f'\nO item {item} precisa ser comprado!')

