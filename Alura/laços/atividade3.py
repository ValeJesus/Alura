contador = 0

while contador < 10:
    print("Processando dados...")

#No código apresentado não há fim porque o contador sempre será 0, e o while vai printar a mensagem enquanto o contador for menor que 10, fazendo com que se torne um loop infinito. A solução seria adicionar um valor ao contador toda vez que a mensagem apareça

#Solução:

contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1