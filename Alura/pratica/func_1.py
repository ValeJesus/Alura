def calcular_gorjeta(valor):
    gorjeta = valor * 0.10
    total = valor + gorjeta
    return gorjeta, total

def escolher(valor):
    gorjetaperc = float(input(f'Quanto você deseja pagar de gorgejeta (ex: 15% --> 0.15): '))
    gorjeta = valor * gorjetaperc
    total = valor + gorjeta
    return gorjeta,total
    
