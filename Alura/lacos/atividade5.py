projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for i, projeto in enumerate(projetos):
    

    if projeto == None:
        projetos[i] = 'Projeto ausente'

print(projetos)


