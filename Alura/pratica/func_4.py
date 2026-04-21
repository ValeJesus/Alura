def contar(texto):
    split = texto.split()
    contador = 0
    palavras = []

    for s in split:
        if len(s) > 10:
            contador += 1
            palavras.append(s)
            

    print(f'As palavras que tem main de 10 letras são:  {palavras} ')

    



