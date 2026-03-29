from func_1 import calcular_gorjeta
from func_1 import escolher

valor = int(input('\nDigite o valor da conta: '))
escolha = input(f'\nVocê deseja pagar 10% ou quer escolher outro valor (S ou N): ')

if escolha == 's' or escolha == 'S':
    gorjeta, total= calcular_gorjeta(valor)
    
elif escolha == 'n' or escolha == 'N':
    gorjeta, total = escolher(valor)
    



print(f'Valor da gorjeta: {gorjeta} \n Total a pagar: {total}')