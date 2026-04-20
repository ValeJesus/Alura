def coleta():
    num = input('nums separados por um espaço: ').split()

    pares = filter(lambda x:int(x) % 2 == 0, num)
    print("Números pares:", " ".join(pares)) 
coleta()



