
convidados = set()  # Cria um conjunto vazio para armazenar nomes únicos

while True:
    nome = input("Digite o nome do convidado ou 'sair' para encerrar: ")

    # Se o usuário digitar 'sair' (maiúsculas/minúsculas indiferente), interrompe o loop
    if nome.lower() == "sair":
        break

    # Adiciona o nome ao conjunto (duplicatas são automaticamente ignoradas)
    convidados.add(nome)

# Exibe todos os convidados confirmados em uma única linha separados por vírgulas
print(f"Convidados confirmados: {', '.join(convidados)}")

    